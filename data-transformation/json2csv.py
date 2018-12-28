#!/usr/bin/env python2

import sys
import unicodecsv as csv
import json

# read data from STDIN
input_str = sys.stdin.read()

# parse data as a json
data = json.loads(input_str)

# first row
first_row = data[0]

# set the column names of csv to the "keys" in the first row
fieldnames = list(first_row.keys())

# use python's csv library to create a csv writer
writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)

# write the column headers of csv
writer.writeheader()

# write remaining rows
writer.writerows(data)
