import requests

token = 'TOKEN'
url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(token)}
params = {"path": 'Test05_23_03_2022', "overwrite": "true"}

'''Test_01. Добавление папки на Яндекс Диск. Метод Put'''

response = requests.put(url, headers=headers, params=params)
print(f'Status Code = {response.status_code}')
if response.status_code == 201:
       print(f'{params["path"]} adding successful. Test is pass')
else:
       print(f'Adding {params["path"]} Test_01 is fail')
       print(response.text)
       print(response.headers)
       exit(2)

'''Test_02. Удаление папки на Яндекс Диск. Метод Delete'''

response = requests.delete(url, headers=headers, params=params)
print(f'Status Code = {response.status_code}')
if response.status_code == 204:
       print(f'{params["path"]} deleted successful. Test is pass')
else:
       print(f'Deleting folder {params["path"]} is fail')
       print(response.text)
       print(response.headers)
       exit(2)

