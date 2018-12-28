#!/usr/bin/env python2

import sys
import csv
import json

# read data from STDIN and split on each newline
data = sys.stdin.read().splitlines()

# use python's csv library to create a csv reader
reader = csv.DictReader(data)

# get list of rows from reader
rows = list(reader)

# output json
json.dump(rows, sys.stdout, indent=4)
