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
        # pprint(result)
        img_url_list = []
        img_url_dict = {}
        for i in result['response']['items']:
            size = 0
            for j in i['sizes']:
                if j['height'] > size:
                    size = j['height']
                    img_url = j['url']
            img_url_list.append(img_url)
        return img_url_list

    def up_photos(self, ls, dir):
        #Создание папки
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {"path": dir}
        with open('ya_token.txt') as f:
            self.token = f.read().strip()
        headers = {"Authorization": self.token}
        resp = requests.put(url, params=params, headers=headers)
        #print(resp.status_code)
        #Загрузка файлов
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        for i, j in enumerate(ls):
            path = dir+ '/'+dir + '-' + str(i)
            params = {"path": path}
            headers = {"Authorization": self.token}
            resp = requests.get(url, params=params, headers=headers)
            print(resp.status_code)
            # print(resp.json())


            url_up = resp.json()['href']
            image = requests.get(j)
            up_file = requests.put(url_up, image.content)
            print(up_file.status_code)


vk_client = VkUser('552934290')
dir_name = vk_client.user_info()
#pprint(dir_name)
img_list = vk_client.get_url_photos()
#pprint(img_list)
vk_client.up_photos(img_list, dir_name)