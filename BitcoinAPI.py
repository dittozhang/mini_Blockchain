import requests
import json


def showBBH(height):  # Bitcoin block height
    request = requests.get('https://blockchain.info/block-height/'
                           + str(1) + '?format=json')
    print(json.dumps(json.loads(request.text), indent=4, sort_keys=True))
