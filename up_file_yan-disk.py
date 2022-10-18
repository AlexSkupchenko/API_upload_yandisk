import json
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path, file):
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json',
                   'Authorization': f'OAuth {self.token}'
                   }
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": file_path,
                  "overwrite": "true"
                  }
        response = requests.get(url, headers = headers, params = params)
        res = response.json()
        response = requests.put(res['href'], data = open(file, 'rb'))

if __name__ == '__main__':
    path_to_file = 'nonsense\riddle.txt'
    token = '...'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, 'riddle.txt')