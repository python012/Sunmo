#!/usr/bin/env python3

import configparser
import os
import sys


# base_path = None
# if os.name == 'nt':
#     base_path = os.path.dirname(os.path.abspath(__file__)) + '\\..\\'
# else:
#     base_path = os.path.dirname(os.path.abspath(__file__)) + '/'

# sys.path.append(base_path)

# config_path = os.path.join(base_path, 'config', 'config.ini')

# config = configparser.ConfigParser()
# config.read(config_path)

# MAC_CHROME_DRIVER_PATH = config['win']['chrome_driver_path']

class ConfigReader(object):

    def __init__(self, base_path):
        self.__config_path = os.path.join(base_path, 'config', 'config.ini')
        if os.path.exists(self.__config_path):
            self.config = configparser.ConfigParser()
            self.config.read(self.__config_path)
        else:
            raise FileNotFoundError(
                'Config file is NOT present as "' + self.__config_path + '" !')

    def get_mac_chrome_driver(self):
        return self.config['mac']['chrome_driver_path']

    def get_win_chrome_driver(self):
        return self.config['win']['chrome_driver_path']
