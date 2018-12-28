#!/usr/bin/env python2

import sys
import csv
import json

# read data from STDIN
input_str = sys.stdin.read()

# parse data as a json
data = json.loads(input_str)

new_data = []
for row in data:
    new_row = {
        "bioguide": row['id']['bioguide'],
        "first": row['name']['first'],
        "last": row['name']['last'],
        "full": row['name']['official_full'],
        "birthday": row['bio']['birthday'],
        "gender": row['bio']['gender'],
        "religion": row['bio'].get('religion'),
        "party": row['terms'][-1]['party'],
        "state": row['terms'][-1]['state']
    }
    new_data.append(new_row)

sys.stdout.write(json.dumps(new_data))
