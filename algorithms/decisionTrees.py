#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from dateutil import parser
from tempfile import TemporaryFile
import numpy as np
from algorithms import decisionnode

def getcat(category):
    with open("data/treedata.json") as data_file:
        data = json.load(data_file)
        for sample in data["trees"]:
            if(sample["category"] == category):
                return sample

def constructMatrix(category, pages):
    params = getcat(category)["parameters"]
    mat = [[0 for x in range(len(params)+1)] for y in range(len(pages))]
    print mat
    x = 0
    for page in pages:
        y = 0
        for param in params:
            if(param["type"] == "fl"):
                place = page.value.splitlines()[0]
                #mat[x][y] = 1 if param["term"] in page.splitlines()[0] else 0
            if(param["type"] == "all"):
                place = page.value
                #mat[x][y] = 1 if param["term"] in page else 0
            if(param["term"] == "{n}"):
                print str(x) + ", " + str(y)
                mat[x][y] = 1 if any(char.isdigit() for char in place) else 0
            elif(param["term"] == "{d}"):
                print str(x) + ", " + str(y)
                mat[x][y] = 1 if parser.parse(place, fuzzy=True) else 0
            elif("," in param["term"]):
                terms = param["term"].split(",")
                mat[x][y] = 1 if all(x in place for x in terms) else 0
            elif("/" in param["term"]):
                terms = param["term"].split("/")
                mat[x][y] = 1 if any(x in place for x in terms) else 0
            else:
                print str(x) + ", " + str(y)
                mat[x][y] = 1 if param["term"] in place else 0
            y+=1
        mat[x][y] = page.isTrue
        x+=1
    print mat
    #outfile = TemporaryFile()
    np.save("mat", mat)
    return mat

def divideset(rows,column,value):
    split_function=None
    if isinstance(value,int) or isinstance(value,float):
        split_function=lambda row:row[column]>=value
    else:
        split_function=lambda row:row[column]==value
    set1=[row for row in rows if split_function(row)]
    set2=[row for row in rows if not split_function(row)]
    return (set1,set2)
def uniquecounts(rows):
    results={}
    for row in rows:
        r=row[len(row)-1]
        if r not in results: results[r]=0
        results[r]+=1
    return results
def entropy(rows):
    from math import log
    log2=lambda x:log(x)/log(2)
    results=uniquecounts(rows)
    ent = 0.0
    for r in results.keys():
        p=float(results[r])/len(rows)
        ent=ent-p*log2(p)
    return ent
def buildtree(rows, score=entropy):
    if len(rows) == 0: return decisionnode()
    current_score = score(rows)

    best_gain = 0.0
    best_criteria = None
    best_sets = None

    column_count = len(rows[0]) - 1 #last column is result
    for col in range(0, column_count):
        column_values = set([row[col] for row in rows])
        for value in column_values:
            set1, set2 = divideset(rows, col, value)
            p = float(len(set1))/len(rows)
            gain = current_score - p*score(set1) - (1-p)*score(set2)
            if gain>best_gain and len(set1) > 0 and len(set2) > 0:
                best_gain = gain
                best_criteria = (col, value)
                best_sets = (set1, set2)
    if best_gain > 0:
        trueBranch = buildtree(best_sets[0])
        falseBranch = buildtree(best_sets[1])
        return decisionnode(col=best_criteria[0], value=best_criteria[1], tb=trueBranch, fb=falseBranch)
    else:
        return decisionnode(results = uniquecounts(rows))
def printtree(tree,indent=""):
    if tree.results!=None:
        print str(tree.results)
    else:
        print 'Column' + str(tree.col) + ' : ' + str(tree.value) + '? '
        print indent+'True->',
        printtree(tree.tb,indent+'    ')
        print indent+'False->',
        printtree(tree.fb,indent+'    ')
