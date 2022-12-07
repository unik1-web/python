from os import system
system("curl -X 'POST' \  'https://api.reo.ru/reo-weight-control-api/api/v1/weight-controls/import' \  -H 'accept: */*' \  -H 'Content-Type: multipart/form-data' \  -F 'file='")
