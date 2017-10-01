#!/usr/bin/python
import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

    if line[0] == 'id':
    	continue	

    tags = 	line[2]

    tags_split = re.split('[" "]', tags)

    tags_split = filter(None, tags_split) #removing empty tags

    for i in range(0, len(tags_split)):
		
		print "{0}\t{1}".format(tags_split[i], 1)