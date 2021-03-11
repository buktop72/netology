import requests
import logging
import json
from pprint import pprint

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename='debug.log',
    filemode='w'
)
logger = logging.getLogger()


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
        logging.debug('Start user_info')
        url = 'https://api.vk.com/method/users.get'
        params = {
            'user_id': self.id,
            'access_token': self.token,
            'v': '5.130'
        }
        info = requests.get(url, params=params)
        # pprint(info.json())
        return str(info.json()['response'][0]['first_name'] + info.json()['response'][0]['last_name'])

    def get_url_photos(self, count = 5):
        logging.debug('Start get_url_photos')
        res = requests.get(self.url, params=self.params)
        result = res.json()
        # pprint(result)
        json_dict = {}
        json_list = []
        key_list = []
        x = 2
        for i in result['response']['items']:
            size = 0
            print('длина', len(json_list))
            if len(json_list) <= count-1:
                for j in i['sizes']:
                    if j['height'] > size:
                        size = j['height']
                        img_url = j['url']
                        json_dict['size'] = j['type']
                        json_dict['url'] = img_url
                key = str(i["likes"]['count'])
                key_list.append(key)
                if key_list.count(key) > 1:
                    json_dict['name'] = f"{key}-{x}.jpg"
                    x += 1
                else:
                    json_dict['name'] = f"{key}.jpg"
                json_list.append(json_dict.copy())
            else:
                break
        return json_list

    def list_dir(self):
        logging.debug('Start list_dir')
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': '/'}
        with open('ya_token.txt') as f:
            self.token = f.read().strip()
        headers = {"Authorization": self.token}
        resp = requests.get(url, params=params, headers=headers)
        ls_dir = []
        for i in resp.json()['_embedded']['items']:
            ls_dir.append(i['name'])
        print(f"Получено {len(ls_dir)} файлов!")
        logging.debug(f"Получено {len(ls_dir)} файлов!")
        return ls_dir

    def up_photos(self, dict, dir, ls_dir):
        # dict - список словарей - name,size, url
        # dir
        # list_dir -список папок на YaDisk
        # ls_dir - то же, что list_dir ???
        dict_lite = {}
        list_dict_lite = []
        for i in dict:
            dict_lite['file_name'] = i['name']
            dict_lite['size'] = i['size']
            list_dict_lite.append(dict_lite.copy())
        # print(list_dict_lite)
        with open("vk.json", "w", encoding="utf-8") as f:
        	json.dump(list_dict_lite, f, ensure_ascii=False, indent=2)


        # pprint(dict)
        # logging.debug('Start up_photos')
        # создание папки на YaDisk:
        if dir not in ls_dir:
            url = 'https://cloud-api.yandex.net/v1/disk/resources'
            params = {"path": dir}
            with open('ya_token.txt') as f:
                self.token = f.read().strip()
            headers = {"Authorization": self.token}
            resp = requests.put(url, params=params, headers=headers)
            if resp.status_code:
                logging.debug(f"Каталог {dir} создан!")
        else:
            print(f"Каталог {dir} уже существует!")
            logging.debug(f"Каталог {dir} уже существует!")
            exit()
        # Загрузка файлов на YaDisk, в созданную папку:
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        for i in dict:
            # Получение ссылки для закачки файла на YaDisk:
            path = f"{dir}/{i['name']}"
            params = {"path": path}
            headers = {"Authorization": self.token}
            resp = requests.get(url, params=params, headers=headers)
            print(resp.status_code)
            print(resp.json()['href'])
            # logging.debug(resp.status_code)
            url_up = resp.json()['href']
            # print(url_up)
            # Загрузка файла на YaDisk:
            image = requests.get(i['url'])
            up_file = requests.put(url_up, image.content)
            print(up_file.status_code)
            logging.debug(up_file.status_code)
            if up_file.status_code:
                print(f"файл '{i['name']}' загружен в папку '{dir}'")
                logging.debug(f"файл '{i['name']}' загружен в папку '{dir}'")


vk_client = VkUser('552934290')
dir_name = vk_client.user_info()
img_dict = vk_client.get_url_photos()
ls_dir = vk_client.list_dir()
vk_client.up_photos(img_dict, dir_name, ls_dir)
