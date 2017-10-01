#!/usr/bin/python
import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

    author_id = line[3]

    time_added = line[8]

    time_added_split = re.split('[" ":]', time_added)
    
    hour = time_added_split[1]
    
    print time_added_split
    
    print hour
