#!/usr/bin/python
__author__ = 'ioparaskev'

from target_class import target as tar


def print_help():
    print('List of valid commands:\n    [scan] for simple scan, '
          '\n    [scan -v] for more options in scanning'
          '\n    [help] for this message')


if __name__ == '__main__':
    case = input('Enter a command or type help and press enter:\n')
    if case == 'help':
        print_help()
    elif 'scan' in case:
        name = input('Enter ip or url to scan\n')
        #create new Target
        target = tar.Target(name)
        print('Enter a range of ports or ports seperated by comma')
        print('[port range: 40-120 or port numbers: 21,80]')
        ports_input = input()
        try:
            ports_list = tar.create_ports_list(ports_input)
            target.set_port_numbers(ports_list)
        except ValueError:
            print('Wrong port range given')
            exit(1)
        #todo more options for scan (set timeout, change scan type)
        if case == 'scan -v':
            print('Select timeout')
        # target_class.target_description()
        tar.start_scan(target)
        print('Scan completed')
    else:
        print('Wrong command...\nExiting')
        print_help()
        exit(1)