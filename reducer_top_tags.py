#!/usr/bin/python

import sys
import operator

countTotal = 0
tags_dict = {}
oldTag = None


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
       # Something has gone wrong. Skip this line.
        continue

    thisTag, thisCount = data_mapped

    if oldTag and oldTag != thisTag:

    	tags_dict[oldTag] = countTotal

    	oldTag = thisTag
    	countTotal = 0


    oldTag = thisTag

    countTotal += int(thisCount)

if oldTag != None:

	tags_dict[oldTag] = countTotal 


tags_dict_sorted = sorted(tags_dict.items(), key = operator.itemgetter(1), reverse = True)

top10 = tags_dict_sorted[:10]	  

for i in range(0, len(top10)):

	print top10[i][0], "\t", top10[i][1]

    