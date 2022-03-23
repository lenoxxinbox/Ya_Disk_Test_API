import requests

# Test_01. Добавление папки на Яндекс Диск. Метод Put

token = 'TOKEN'
url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(token)}
params = {"path": 'Test05_23_03_2022', "overwrite": "true"}
response = requests.put(url, headers=headers, params=params)
print(f'Status Code = {response.status_code}')
if response.status_code == 201:
       print(f'{params["path"]} adding successful. Test is pass')
else:
       print(f'Adding {params["path"]} Test_01 is fail')
       exit(2)

# Test_02. Удаление папки на Яндекс Диск. Метод Delete

url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(token)}
params = {"path": 'Test05_23_03_2022', "overwrite": "true"}
response = requests.delete(url, headers=headers, params=params)
print(f'Status Code = {response.status_code}')
if response.status_code == 204:
       print(f'{params["path"]} deleted successful. Test is pass')
else:
       print(f'Deleted {params["path"]} Test_02 is fail')
       exit(2)

