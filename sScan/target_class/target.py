__author__ = 'ioparaskev'
from socket import *
from . import connect


class Target:
    """
        Target class variables:
            name: the name
    """
    name = 'google'
    time = 60
    ports = 80
    scantype = 'normal'
    ip = 21
    hostname = name

    def __init__(self, name):
        self.name = name

    def set_hostname(self, name):
        self.hostname = name

    def get_name(self):
        return self.hostname

    def set_timeout(self, time):
        try:
            self.time = time
        except ValueError as val:
            print(val)
            print('Timeout must be a number')
            exit(1)

    def get_timeout(self):
        return self.time

    def set_scantype(self, scantype):
        self.scantype = scantype

    def get_scantype(self):
        return self.scantype

    def set_port_numbers(self, ports):
        self.ports = ports

    def get_port_numbers(self):
        return self.ports

    def set_ip(self, ip):
        self.ip = ip

    def get_ip(self):
        return self.ip

    def target_description(self):
        print('Target name:{}\n'
              'hostname:{}\n'
              'ip:{}\n'
              'ports:{}\n'
              'scantype:{}\n'
              'timeout:{}\n'.format(self.name, self.hostname, self.ip, self.ports, self.scantype, self.time))


def is_ip(name):
    if name.replace('.', '').isnumeric():
        return True


def create_ports_list(ports):
    if '-' in ports:
        ports_input = [int(i) for i in ports.split('-')]
        print(ports_input)
        ports_list = range(min(ports_input), max(ports_input)+1)
    elif ports.replace(',', '').isnumeric():
        ports_list = [int(i) for i in ports.split(',')]
        ports_list = sorted(ports_list)
        print(ports_list)
    else:
        raise ValueError
    return ports_list


def resolve(target):
    """
    :param target: Target object containing information about target_class(name,ip,ports,scan type,timeout)
    :return: list of ips found for target_class name
    """
    try:
        """
            replaced target_ip because gethostbyaddr contains list of ips(better)
            target_ip = gethostbyname(target_class.name)
        """
        target_info = gethostbyaddr(target.name)
        if not is_ip(target.name):
            target.set_hostname(target_info[0])
            print('True host name is: {}'.format(target_info[0]))
            print('Relevant ip list found:')
            for ip in target_info[2]:
                print('    {}\n\n'.format(ip))
        return target_info[2]
    except herror:
        print('cannot resolve {}'.format(target.name))
        print('host resolution error\nexiting...')
        exit(1)


def start_scan(target):
    """
    :param target: Target oject
    :return: no return, initiates the scan
    """
    target.set_ip(resolve(target))
    print('Initiating scan....')
    for ip in target.ip:
        print('  Ip:{}'.format(ip))
        for port in target.ports:
            connect.connect_scan(ip, port)


def main():
    pass

if __name__ == '__main__':
    main()