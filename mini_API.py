# control
import requests
import os
import Host_functions


def pingHosts(hosts):    # test all host online or not
    url = 'http://127.0.0.1:'
    print('HOST:')
    for host in hosts:
        if requests.get(url+host+'/chain').status_code\
                == requests.codes.ok:
            print('host: {0:<5}\tonline'.format(host))
        else:
            print('host: {0:<5}\toffline'.format(host))


def hosts_View(hosts):
    print('###########')
    for index in range(len(hosts)):
        print('# {}. {} #'.format(index, hosts[index]))
    print('###########')


def function_View():
    functions = ['Chain', 'Mine', 'Register', 'Resolve', 'Transaction']
    for index in range(len(functions)):
        print('{}. {} '.format(index, functions[index]))


def function_Select(select, host):
    if select == 0:
        Chain()
    elif select == 1:
        Mine()
    elif select == 2:
        Register()
    elif select == 3:
        Resolve()
    elif select == 4
        
    elif select == 5:
            Transaction()


def addHost(hosts):
    host_name = str(len(hosts)+5000)
    os.system('start web.py -P ' + host_name)
    return host_name


hosts = []
nickname = ['Alice', 'Ben', 'Carl', 'David', 'Eva', 'Frank', 'Gina']
move = -1


while True:
    os.system('cls')
    if len(hosts) == 0:
        if str.upper(input('no server for now, do you want to buid one?\nY/N\n'))\
                == 'Y':
            num = int(input('how much?\n'))
            for n in range(num):
                hosts.append(addHost(hosts))  # add new host
            continue
        else:
            break

    hosts_View(hosts)
    function_View()
    move = int(input('Choose function:'))
    host = int(input('Which host:'))
