#!/usr/bin/python

import sys

from collections import Counter

hourList = []
oldKey = None


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHour = data_mapped

    if oldKey and oldKey != thisKey:
    
      data = Counter(hourList)
      ans = data.most_common(len(hourList))
      count = 1
      for i in range(0, len(ans)):
    
          if i < len(ans) - 1:
              if (ans[i][1] == ans[i+1][1]):
                   count = count + 1  
              else:
                break
          else:
            count = len(ans)
            
      for i in range(0, count):   
      
        hourMost = data.most_common(count)[i][0]
        print oldKey, "\t", hourMost
        
      oldKey = thisKey;
      hourList = []

    oldKey = thisKey

    hourList.append(thisHour)

if oldKey != None:
    data = Counter(hourList)
      
    ans = data.most_common(len(hourList))

    count = 1
  
    for i in range(0, len(ans)):
    
      if i < len(ans) - 1:
          if (ans[i][1] == ans[i+1][1]):
              count = count + 1  
          else:
              break
      else:
          count = len(ans)
            
    for i in range(0, count):    
      
      hourMost = data.most_common(count)[i][0]
      print oldKey, "\t", hourMost


