import requests

# Test_01. Добавление папки на Яндекс Диск. Метод Put

token = 'AQAAAABevsvRAADLW3vfon47DkCLi2tqFwuOTWc'
url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(token)}
params = {"path": 'Test05_23_03_2022', "overwrite": "true"}
response = requests.put(url, headers=headers, params=params)
print(f'Status Code = {response.status_code}')
if response.status_code == 201:
       print(f'{params["path"]} download successful. Test is pass')
else:
       print('Test is fail')

# Test_02. Удаление папки на Яндекс Диск. Метод Delete

url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(token)}
params = {"path": 'Test05_23_03_2022', "overwrite": "true"}
response = requests.delete(url, headers=headers, params=params)
print(f'Status Code = {response.status_code}')
if response.status_code == 204:
       print(f'{params["path"]} download successful. Test is pass')
else:
       print('Test is fail')
