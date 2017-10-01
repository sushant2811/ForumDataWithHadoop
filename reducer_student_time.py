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
    	hourMost = data.most_common(1)[0][0]
        print oldKey, "\t", hourMost
        
        oldKey = thisKey;
        hourList = []

    oldKey = thisKey

    hourList.append(thisHour)

if oldKey != None:
    data = Counter(hourList)
    hourMost = data.most_common(1)[0][0]
    print oldKey, "\t", hourMost


