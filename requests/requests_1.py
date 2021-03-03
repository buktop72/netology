import requests

def calc_intellect(ls):
    dict_intell = {}
    for i in ls:
        url = 'https://superheroapi.com/api/2619421814940190/search/' + i
        response = requests.get(url)
        dict_intell[i] = (response.json()['results'][0]['powerstats']['intelligence'])
    key_max = max(dict_intell)
    print('Наибольший интеллект имеет', key_max, '-', dict_intell[key_max])


calc_intellect(['Hulk', 'Captain America', 'Thanos'])