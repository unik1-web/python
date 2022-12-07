import requests
response = requests.post('http://httpbin.org/post', files=dict(foo='bar'))
response.status_code
from pprint import pprint
pprint(response.json()['headers'])
