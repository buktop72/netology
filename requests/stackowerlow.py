import requests
from datetime import datetime
from pprint import pprint

def python_tags(tag):
    d = datetime.today()
    to_date = str(round(d.timestamp()))
    from_date = str(round(d.timestamp()-259200))
    url = 'https://api.stackexchange.com/2.2/questions'
    params = {'fromdate':from_date, 'todate':to_date, 'order':'desc', 'sort':'activity', 'tagged':tag,
             'site':'stackoverflow.com'}
    resp = requests.get(url, params = params)
    dict = (resp.json())
    for i in dict['items']:
        print(i['title'])

python_tags('python')