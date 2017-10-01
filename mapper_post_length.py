#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

    if line[0] == 'id':
    	continue

    if line[5] == 'question':
    
    	print "{0}\t{1}\t{2}".format(line[0], line[5], len(line[4]))

    if line[5] == 'answer':

    	print "{0}\t{1}\t{2}".format(line[6], line[5], len(line[4]))			

