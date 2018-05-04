#!/usr/bin/env python3

import os
import sys

base_path = None
if os.name == 'nt':
    base_path = os.path.dirname(os.path.abspath(__file__)) + '\\..\\'
else:
    base_path = os.path.dirname(os.path.abspath(__file__)) + '/'

sys.path.append(base_path)
print(base_path + 'utils')

from utils import config_reader

from utils.config_reader import ConfigReader

print(ConfigReader)
# print(config_reader.get_mac_chrome_driver(base_path))