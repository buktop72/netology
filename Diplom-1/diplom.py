import requests
from pprint import pprint
"""
image = request.get(image_url) 
запрос по url картинки, то есть получаем картинку по url.

request.put(url = ссылка для загрузки на ядиск, image.content = картинка для загрузки) 
кладем картинку на ядиск
"""

with open('token.txt') as f:
    token = f.read().strip()
    # print(token)
URL = 'https://api.vk.com/method/users.get'
params = {
    'user_id': '552934290',
    'access_token': token,
    'v': '5.130'
}
res = requests.get(URL, params=params)
res.json()
# pprint(res.json()) #инфо о юзере

URL = 'https://api.vk.com/method/photos.get'
params = {
    'owner_id': '552934290',
    'access_token': token,
    'album_id': 'profile',
    'rev': '0',
    'extended': '1',
    'v': '5.130'
}
res = requests.get(URL, params=params)
rezult = res.json()
img_url_list = []
img_url_dict = {}

for i in rezult['response']['items']:
    size = 0
    for j in i['sizes']:
        if j['height'] > size:
            size = j['height']
            img_url = j['url']
    img_url_list.append(img_url)
pprint(img_url_list)

# Загрузка на диск
url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
for i, j in enumerate(img_url_list):
    # print(i)
    path = 'image-' + str(i)
    # print(path)
    params = {"path": path}
    headers = {"Authorization": 'AgAAAAAA6fCKAADLW5ySBte9PUfbgJ5nN8R7VTo'}
    resp = requests.get(url, params=params, headers=headers)
    print(resp.status_code)

    url_up = resp.json()['href']
    image = requests.get(j)
    up_file = requests.put(url_up , image.content)
    # with open('python.jpg', 'rb') as f:
    #      up_file = requests.put(url_up, files={"file": f})
    print(up_file.status_code)
