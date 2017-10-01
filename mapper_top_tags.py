#!/usr/bin/python
import sys
import csv
import re

import operator

reader = csv.reader(sys.stdin, delimiter='\t')

tags_dict = {}

for line in reader:

    if line[0] == 'id':
    	continue	

    tags = 	line[2]

    tags_split = re.split('[" "]', tags)

    tags_split = filter(None, tags_split) #removing empty tags

    for i in range(0, len(tags_split)):
		
		if tags_split[i] in tags_dict:

			tags_dict[tags_split[i]] += 1

		else:

			tags_dict[tags_split[i]] = 1

tags_dict_sorted = sorted(tags_dict.items(), key = operator.itemgetter(1), reverse = True)

top10 = tags_dict_sorted[:10]

for i in range(0, len(top10)):

	print "{0}\t{1}".format(top10[i][0], top10[i][1])
