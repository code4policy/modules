import requests
import json

# base url for specific api
base_url = 'https://elections.huffingtonpost.com/pollster/api/v2/'

# operation to execute for the api
operation = 'polls'

# additional api parameters specific to the operation
api_parameters = {'sort':'updated_at'}

# ping api
response = requests.get(base_url + operation, params = api_parameters)

# print status code and load returned data into json
print('Response Code: {0}\n'.format(response.status_code))
data = json.loads(response.text)

# save raw data
with open('huffpost_api_results.json', 'w') as outfile:
    json.dump(data, outfile)

# print url for each poll
for poll in data['items']:
    print(poll['url'])