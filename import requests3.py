import requests
url = 'https://httpbin.org/post'
#files = {'file': ('file.txt')}
#response = requests.post(url, files=files)
#print(response.text)
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
response = requests.post(url, files=files)

print(response.text)