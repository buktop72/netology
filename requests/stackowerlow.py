import requests
from pprint import pprint

def python_tags(from_date, to_date, tag):
    url = 'https://api.stackexchange.com/2.2/questions'
    params = {'fromdate':from_date, 'todate':to_date, 'order':'desc', 'sort':'activity', 'tagged':tag,
             'site':'stackoverflow.com'}
    resp = requests.get(url, params = params)
    dict = (resp.json())
    for i in dict['items']:
        print(i['title'])

python_tags('1614470400','1614729600', 'python')