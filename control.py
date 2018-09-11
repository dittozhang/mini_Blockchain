# control
import requests
import os


def pingHosts(hosts_list):    # test all host online or not
    url = 'http://127.0.0.1:'
    print('HOST:')
    for host in hosts_list:
        if requests.get(url+host+'/chain').status_code\
                == requests.codes.ok:
            print('host: {0:<5}\tonline'.format(host))
        else:
            print('host: {0:<5}\toffline'.format(host))


def host_view(hosts_list):
    for hosts_index in range(len(hosts_list)):
        print('{}. {}'.format(hosts_index, hosts_list[hosts_index]))


def fuction_view():
    function = ['chain', 'mine', 'register', 'resolve']


def addHost(hosts_list):
    host_name = str(len(hosts_list)+5000)
    os.system('start web.py -P ' + host_name)
    return host_name


hosts_list = []

while True:
    pass
