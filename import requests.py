import requests
response = requests.post('https://httpbin.org/post', json={'key':'value'})
json_response = response.json()
json_response['data'] 
'{"key": "value"}'
json_response['headers']['Content-Type'] 
'application/json'
print (response.status_code)
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')