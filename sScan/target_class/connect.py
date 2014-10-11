__author__ = 'ioparaskev'

from socket import *


def connect_scan(target_host, target_port):
    try:
        connect_socket = socket(AF_INET, SOCK_STREAM)
        connect_socket.settimeout(5)
        connect_socket.connect((target_host, target_port))
        print('    [+] {} is open'.format(target_port))
        connect_socket.close()
    except timeout:
        print('    [?] timeout for port {}'.format(target_port))
    except herror:
        print('address resolution error, host is down?')
    except error:
        print('uknown error: {}'.format(error.strerror))
    except (RuntimeError, TypeError, NameError) as exception:
        print('error:{}'.format(exception))