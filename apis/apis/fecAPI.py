import requests
import json
import os

# base url for specific api
base_url = 'https://api.open.fec.gov/v1/'

# operation to execute for the api
operation = 'candidates'

# get key from environment variable
key = os.environ['FECKEY']

# additional api parameters specific to the operation
api_parameters = {'api_key': key, 'office':'H', 'sort':'name', 'state':'MA', 'election_year':[2016]}

# ping api
response = requests.get(base_url + operation, params = api_parameters)

# print status code and load returned data into json
print('Response Code: {0}\n'.format(response.status_code))
data = json.loads(response.text)

# save raw data
with open('fec_api_results.json', 'w') as outfile:
    json.dump(data, outfile)

# loop through results and print name
for candidate in data['results']:
    print(candidate['name'])
