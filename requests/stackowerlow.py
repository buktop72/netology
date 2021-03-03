import requests
from pprint import pprint

def python_tags(url):    
    params = {'fromdate':'1614470400', 'todate':'1614729600', 'order':'desc', 'sort':'activity', 'tagged':'python',
             'site':'stackoverflow.com'}
    resp = requests.get(url, params = params)
    dict = (resp.json())
    for i in dict['items']:
        print(i['title'])

python_tags('https://api.stackexchange.com/2.2/questions')