import requests
from datetime import datetime

with open('token_test.txt', 'r') as file:
    token = file.read().strip()

url_API = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(token)}
params = {"path": 'TestFolder'}
params_f = {'path': 'TestFolder/Test_image',
                        'url': 'https://kartinkin.net/uploads/posts/2021-03/1616125516_57-p-elbrus-krasivie-foto-58.jpg'}
params_c = {'from': 'TestFolder/Test_image', 'path': 'Test_image_00'}
params_l = {'limit': 5}


class YaDiskFolders:

    def __init__(self, url, headers, params):
        self.url = url_API
        self.headers = headers
        self.params = params

    def test_append_folder(self):
        """Test_01. Создание папки на YandexDisk. Метод Put"""
        print()
        response = requests.put(url_API, headers=headers, params=params)
        print('Test_01. Creating a Folder on YandexDisk. Put method')
        print(f'Status Code = {response.status_code}')
        if response.status_code == 201:
            print(f'{params["path"]} adding successful. Test is pass')
            report = f'{datetime.now()} TEST IS PASS! The Folder {params["path"]} is appended on the YaDisk\n' \
                     f'Status_code = {response.status_code}\n'
            with open('report.txt', 'a') as rep:
                rep.write(report)
        else:
            print(f'Adding {params["path"]} Test_01 is fail')
            print(response.text)
            print(response.headers)
            report = f'{datetime.now()} TEST IS FAILED! The Folder {params["path"]} IS NOT appended on the YaDisk\n' \
                     f'Status_code = {response.status_code}\n'
            with open('report.txt', 'a') as rep:
                rep.write(report)
            # exit(2)

    def test_download_file(self):
        """Test_02. Загрузка файла в папку на YandexDisk. Метод Post"""
        print()
        download_file = requests.post(url=url_API + '/upload', headers=headers, params=params_f)
        print('Test_02. Uploading a file to a Folder on YandexDisk. Post Method')
        print(f'Status Code = {download_file.status_code}')
        if download_file.status_code == 202:
            print(f'{params_f["path"]} downloading successful. Test is pass')
            report = f'{datetime.now()} TEST IS PASS! The file {params_f["path"]} is downloading on the YaDisk\n' \
                     f'Status_code = {download_file.status_code}\n'
            with open('report.txt', 'a') as rep:
                rep.write(report)
        else:
            print(f'Downloading file {params_f["path"]} is fail')
            print(download_file.text)
            print(download_file.headers)
            report = f'{datetime.now()} TEST IS FAILED! The file {params_f["path"]} ' \
                     f'IS NOT downloading on the YaDisk\n' \
                     f'Status_code = {download_file.status_code}\n'
            with open('report.txt', 'a') as rep:
                rep.write(report)

    def test_copy_file(self):
        """Test_03. Копирование файла в папку на YandexDisk. Метод Post"""
        print()
        copy_file = requests.post(url=url_API + '/copy', headers=headers, params=params_c)
        print('Test_03. Copying a file to a Folder on YandexDisk. Post Method')
        print(f'Status Code = {copy_file.status_code}')
        if copy_file.status_code == 201:
            print(f'{params_c["path"]} copying successful. Test is pass')
            report = f'{datetime.now()} TEST IS PASS! The file {params_c["path"]} is copying on the YaDisk\n' \
                     f'Status_code = {copy_file.status_code}\n'
            with open('report.txt', 'a') as rep:
                rep.write(report)
        else:
            print(f'Downloading file {params_f["path"]} is fail')
            print(copy_file.text)
            print(copy_file.headers)
            report = f'{datetime.now()} TEST IS FAILED! The file {params_c["path"]} ' \
                     f'IS NOT copying on the YaDisk\n' \
                     f'Status_code = {copy_file.status_code}\n'
            with open('report.txt', 'a') as rep:
                rep.write(report)

    def test_file_list(self):
        """Тест_04. Получение списка файлов YandexDisk. Метод Get"""
        print()
        resp = requests.get(url=url_API + '/files', headers=headers, params=params_l)
        print('Test_04. Getting a list of YandexDisk files. Get Method')
        print(f'Status Code = {resp.status_code}')
        if resp.status_code == 200:
            print('List generated. Test is pass')
            list_file = resp.json()['items']
            for unit in list_file:
                name = unit['name']
            report = f'{datetime.now()} TEST IS PASS! List of files generated\n' \
                     f'Status_code = {resp.status_code}\n' \
                     f'{name}\n'

            with open('report.txt', 'a') as rep:
                rep.write(report)
        else:
            print('List is not generated. Test is fail')
            print(resp.text)
            print(resp.headers)
            report = f'{datetime.now()} TEST IS FAILED! List of files is not generated\n' \
                     f'Status_code = {resp.status_code}\n'
            with open('report.txt', 'a') as rep:
                rep.write(report)
            # exit(2)

    def test_delete_folder(self):
        """Test_05. Удаление папки c YandexDisk. Метод Delete"""
        print()
        response = requests.delete(url_API, headers=headers, params=params)
        print('Test_05. Deleting the folder with YandexDisk. Delete method')
        print(f'Status Code = {response.status_code}')
        if response.status_code == 200 or 202 or 204:
            print(f'{params["path"]} deleted successful. Test is pass')
            report = f'{datetime.now()} TEST IS PASS! The Folder {params["path"]} is deleted on the YaDisk\n' \
                     f'Status_code = {response.status_code}\n'
            with open('report.txt', 'a') as rep:
                rep.write(report)
        else:
            print(f'Deleting folder {params["path"]} is fail')
            print(response.text)
            print(response.headers)
            report = f'{datetime.now()} TEST IS FAILED! The Folder {params["path"]} IS NOT deleted on the YaDisk\n' \
                     f'Status_code = {response.status_code}\n'
            with open('report.txt', 'a') as rep:
                rep.write(report)
            # exit(2)


def main():
    test_api = YaDiskFolders(url_API, headers, params)

    test_api.test_append_folder()
    test_api.test_file_list()
    test_api.test_download_file()
    test_api.test_file_list()
    test_api.test_copy_file()
    test_api.test_file_list()
    test_api.test_delete_folder()
    test_api.test_file_list()


if __name__ == '__main__':
    main()
