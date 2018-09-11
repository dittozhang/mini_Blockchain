# methods
import json
import requests


def get(index):
    url = 'http://127.0.0.1:5000/'
    print('GET: {}{}'.format(url, index))
    return requests.get(url+index)


def showJson(data):
    return json.dumps(json.loads(data), sort_keys=True, indent=4)


def getAndShow(index):
    print(showJson(get(index).text))


def
