#!/usr/bin/env python2

import sys
import requests
import unicodecsv as csv

response = requests.get("https://theunitedstates.io/congress-legislators/legislators-current.json")
data = response.json()

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

first_row = new_data[0]

fieldnames = list(first_row.keys())

# use python's csv library to create a csv writer
writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)

# write the column headers of csv
writer.writeheader()

# write remaining rows
writer.writerows(new_data)
