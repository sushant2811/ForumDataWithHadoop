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

    print len(tags_split)