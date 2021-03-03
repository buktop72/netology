import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {"path": "python_up.jpg"}
        headers = {"Authorization": self.token}
        resp = requests.get(url, params=params, headers=headers)
        print(resp.status_code)

        url_up = resp.json()['href']
        with open('python.jpg', 'rb') as f:
             up_file = requests.put(url_up, files={"file": f})
        print(up_file.status_code)




if __name__ == '__main__':
    uploader = YaUploader("AgAAAAAA6fCKAADLW5ySBte9PUfbgJ5nN8R7VTo")
    result = uploader.upload("python_up.jpg")



