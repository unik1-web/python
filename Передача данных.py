import requests
requests.get('https://api.reo.ru/reo-weight-control-api/api/v1/weight-controls/import' )
response = requests.get('https://api.reo.ru/reo-weight-control-api/api/v1/weight-controls/import' )
if response.status_code == 200:
    print('Запрос успешно обработан')
elif response.status_code == 403:
    print('Ограничение в доступе. Некорректный ключ доступа')
elif response.status_code == 422:
    print('Ошибка валидации')