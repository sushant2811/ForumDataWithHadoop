#!/usr/bin/python
import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

    author_id = line[3]

    time_added = line[8]

    print 'author id: %s' %author_id
    print 'time_added : %s' %time_added	
