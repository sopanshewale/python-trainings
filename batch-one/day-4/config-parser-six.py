#!/usr/bin/python3
from configparser import ConfigParser

parser = ConfigParser()
parser.read('interpolate_configuration.ini')

print (parser.get('Paths', 'my_dir'))

