#!/usr/bin/python
# -*- coding: utf-8 -*-

# encoding=utf8


import sqlite3
import re
import string
import math


class cwe:
    conn = sqlite3.connect('cats.db')
    cursor = conn.cursor()
    whitelist = string.ascii_letters + u"ךםןףץאבגדהוזחטיכלמנסעפצקרשת "

    # Create Words table

    def checkDB(self):
        self.conn.execute("""CREATE TABLE IF NOT EXISTS Words
						(
						ID Integer PRIMARY KEY NOT NULL,
						Category Text NOT NULL,
						Word Text NOT NULL,
						Value Real NOT NULL
						)
						""")
        self.conn.commit()

    # Get all the words with percentage of (greater or equal to a*100 %) to be in a text

    def findSimilarity(self, pages, a):
        sWords = {}
        for page in pages:
            page = ''.join(c for c in page if c in self.whitelist)
            words = []
            for word in page.split():
                if not word in words:
                    words.append(word)
            for word in words:
                if not word in sWords:
                    sWords[word] = 1
                else:
                    sWords[word] = sWords[word] + 1

        # for each word, assign value of it's percentage to be in a text

        sWords.update((x, y * 1.0 / len(pages)) for (x, y) in
                      sWords.items())

        # return all of the words with percentage greater or equal to a*100 %

        return dict((k, v) for (k, v) in sWords.iteritems() if v >= a)

    def insertWords(self, words, category):
        for word in words:
            sql = "INSERT INTO Words (Category, Word, Value) VALUES ('" \
                  + category + "', '" + word + "', " + str(words[word]) \
                  + ')'
            print('Executing: ' + sql)
            self.cursor.execute(sql)
        self.conn.commit()

    def getWords(self, category):
        self.cursor.execute("SELECT Word, Value FROM Words WHERE Category='"
                            + category + "'")
        tmp = {}
        for row in self.cursor:
            tmp[row[0]] = row[1]
        return tmp

    def fixValues(self):
        self.cursor.execute('SELECT Word FROM Words')
        words = {}
        for word in self.cursor:
            if not word in words:
                words[word] = 1
        else:
            words[word] = words[word] + 1
        for word in words:
            self.cursor.execute("SELECT ID, Value FROM Words WHERE Word='"
                                + word[0] + "'")
            rows = self.cursor.fetchall()
            for row in rows:
                newVal = row[1] * math.pow(25, 1.5 - words[word])
                if (newVal < 0.2):  # שרירותי
                    sql = 'DELETE FROM Words WHERE ID=' + str(row[0])
                else:
                    sql = 'UPDATE Words SET Value=' + str(self.translate(newVal, 0, 5, 0, 1)) + ' WHERE ID=' + str(
                        row[0])
                print(sql)
                self.cursor.execute(sql)
        self.conn.commit()

    # return value of page in category - evaluate(string,dict)

    def evaluate(self, page, cat):
        page = ''.join(c for c in page if c in self.whitelist)
        words = page.split()
        value = 0.0
        for word in cat:
            if word in words:
                value = value + cat[word]
        return value

    # get the most evaluated category - getMax(array,dict<dict>)

    def getMax(self, page, cats):
        values = {}
        for cat in cats:
            values[cat] = self.evaluate(page, cats[cat]) / len(cats[cat])
        # print values
        print(values)
        return max(values, key=values.get)

    def resetTable(self):
        sql = "DROP TABLE IF EXISTS Words"
        self.conn.execute(sql)
        self.conn.commit()
        self.checkDB()

    def translate(self, value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)
