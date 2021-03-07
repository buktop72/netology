import requests
from pprint import pprint

class VkUser:
    url = 'https://api.vk.com/method/photos.get'
    def __init__(self, id):
        with open('token.txt') as f:
            self.token = f.read().strip()
        self.id = id
        self.params = {
            'owner_id': self.id,
            'access_token': self.token,
            'album_id': 'profile',
            'rev': '0',
            'extended': '1',
            'v': '5.130'
        }

    def user_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {
            'user_id': self.id,
            'access_token': self.token,
            'v': '5.130'
        }
        info = requests.get(url, params=params)
        return str(info.json()['response'][0]['first_name'] + info.json()['response'][0]['last_name'])

    def get_url_photos(self):
        res = requests.get(self.url, params=self.params)
        result = res.json()
        img_url_list = []
        img_url_dict = {}
        x = 2
        for i in result['response']['items']:
            size = 0
            # pprint(i)
            for j in i['sizes']:
                # pprint(j)
                if j['height'] > size:
                    size = j['height']
                    img_url = j['url']
            img_url_list.append(img_url)
            key = str(i["likes"]['count'])
            if key not in img_url_dict.keys():
                img_url_dict[key] = img_url
            else:
                key = key + '-' + str(x)
                img_url_dict[key] = img_url
                x += 1
        return img_url_dict

    def list_dir(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path' : '/'}
        with open('ya_token.txt') as f:
            self.token = f.read().strip()
        headers = {"Authorization": self.token}
        resp = requests.get(url, params=params, headers=headers)
        ls_dir = []
        for i in resp.json()['_embedded']['items']:
            ls_dir.append(i['name'])
        return ls_dir

    def up_photos(self, dict, dir, list_dir):
        if dir not in ls_dir:
            url = 'https://cloud-api.yandex.net/v1/disk/resources'
            params = {"path": dir}
            with open('ya_token.txt') as f:
                self.token = f.read().strip()
            headers = {"Authorization": self.token}
            resp = requests.put(url, params=params, headers=headers)
        else:
            print(f"Каталог {dir} уже существует!")
            exit()
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        for i in dict:
            path = dir+ '/'+dir + '_' + str(i)
            params = {"path": path}
            headers = {"Authorization": self.token}
            resp = requests.get(url, params=params, headers=headers)
            print(resp.status_code)
            url_up = resp.json()['href']
            image = requests.get(dict[i])
            up_file = requests.put(url_up, image.content)
            print(up_file.status_code)

vk_client = VkUser('552934290')
dir_name = vk_client.user_info()
img_dict = vk_client.get_url_photos()
ls_dir = vk_client.list_dir()
vk_client.up_photos(img_dict, dir_name, ls_dir)
