# How to use treedata.json

| Feature type   | Full name          | Usage  |
| -------------- |:------------------:|:------:|
| fl             | first line         | "fl" : "{term to search in first line}" -- boolean
| all            | whole page         | "all" : "{term to search in the whole page}" -- boolean
| count          | count term in page | "count" : {"location" : "{all/fl}",
|                |                    |           "term" : "{search term}"
|                |                    |          } -- integer
| terms          | "{n}" = search for number
|                | "{d}" = search for date

* if term contains a comma (,) then it'll search for all of the separated terms
* if term contains a slash (/) then it'll search for any of the separated terms
