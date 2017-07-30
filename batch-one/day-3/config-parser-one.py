#!/usr/bin/python3
from configparser import ConfigParser

parser = ConfigParser()
parser.read('sample_configuration.ini')

print(parser.get('session', 'trainer'))
