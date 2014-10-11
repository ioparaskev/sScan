__author__ = 'ioparaskev'

import unittest
from sScan.target_class import target as tar


def start_scan(target):
        tar.start_scan(target)


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # self.target = tar.Target('www.google.com')
        self.target = tar.Target('192.168.2.6')

    def tearDown(self):
        pass

    def test_random_ports(self):
        ports_list = tar.create_ports_list('223,80,443,22,25')
        self.target.set_port_numbers(ports_list)
        start_scan(self.target)



if __name__ == '__main__':
    unittest.main()
