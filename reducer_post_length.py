#!/usr/bin/python

import sys

numberAns = 0
quesLength = 0.0
totalAnsLength = 0.0
meanAnsLength = 0.0
oldKey = None


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
       # Something has gone wrong. Skip this line.
        continue

    thisKey, qorA, len_body = data_mapped

    if oldKey and oldKey != thisKey:

       if numberAns != 0:
       	  meanAnsLength = (totalAnsLength / numberAns)
       else:
       	  meanAnsLength = 0.0 		  
    
       print oldKey, "\t", quesLength, "\t", meanAnsLength

       numberAns = 0 
       quesLength = 0.0
       totalAnsLength = 0.0
       oldKey = thisKey

    oldKey = thisKey

    if qorA == 'question':
    	quesLength = float(len_body)

    if qorA == 'answer':
    	numberAns += 1
    	totalAnsLength += float(len_body)


if oldKey != None:
    if numberAns != 0:
       	  meanAnsLength = (totalAnsLength / numberAns)
    else:
       	  meanAnsLength = 0.0 		  
    
    print oldKey, "\t", quesLength, "\t", meanAnsLength