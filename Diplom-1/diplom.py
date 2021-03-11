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
    # Получаем информацию о юзере (строка "Имя_Фамилия"):
    def user_info(self):
        logging.debug('Start user_info')
        url = 'https://api.vk.com/method/users.get'
        params = {
            'user_id': self.id,
            'access_token': self.token,
            'v': '5.130'
        }
        info = requests.get(url, params=params)
        return str(info.json()['response'][0]['first_name'] +'_'+ info.json()['response'][0]['last_name'])

    # Получаем url фото (список словарей с ключами "name", "size", "url")
    def get_url_photos(self, count = 5):
        logging.debug('Start get_url_photos')
        res = requests.get(self.url, params=self.params)
        result = res.json()
        json_dict = {}
        json_list = []
        like_list = [] # список лайков
        x = 2
        for i in result['response']['items']:
            size = 0
            if len(json_list) <= count-1:
                for j in i['sizes']:
                    if j['height']  * j['width'] > size:
                        size = j['height']  * j['width']
                        print(size)
                        img_url = j['url']
                        json_dict['size'] = j['type']
                        json_dict['url'] = img_url
                like = str(i["likes"]['count'])
                like_list.append(like)
                if like_list.count(like) > 1:
                    json_dict['name'] = f"{like}-{x}.jpg"
                    x += 1
                else:
                    json_dict['name'] = f"{like}.jpg"
                json_list.append(json_dict.copy())
            else:
                break
        return json_list

    # получаем список существующих файлов и папок на YaDisk
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
        logging.debug(f"Получено {len(ls_dir)} файлов!")
        return ls_dir

    # загрузка файлов на YaDisk
    def up_photos(self, dict, dir, ls_dir):
        logging.debug('Start up_photos')
        # dict - список словарей ключами "name", "size", "url"
        # dir - имя создаваемой папки
        # ls_dir - список существующих файлов и папок на YaDisk
        # запись json-файла:
        dict_json = {} # словарь с ключами "name", "size"
        list_dict_json = [] # список словарей dict_json
        for i in dict:
            dict_json['file_name'] = i['name']
            dict_json['size'] = i['size']
            list_dict_json.append(dict_json.copy())
        with open("vk.json", "w", encoding="utf-8") as f:
            json.dump(list_dict_json, f, ensure_ascii=False, indent=2)
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
            logging.debug(resp.status_code)
            url_up = resp.json()['href']
            # Загрузка файла на YaDisk:
            image = requests.get(i['url'])
            up_file = requests.put(url_up, image.content)
            logging.debug(up_file.status_code)
            if up_file.status_code:
                print(f"файл '{i['name']}' загружен в папку '{dir}'")
                logging.debug(f"файл '{i['name']}' загружен в папку '{dir}'")


vk_client = VkUser('552934290')
dir_name = vk_client.user_info()
# Сохранить указанное количество фотографий(по умолчанию 5):
img_dict = vk_client.get_url_photos(10)
ls_dir = vk_client.list_dir()
vk_client.up_photos(img_dict, dir_name, ls_dir)
