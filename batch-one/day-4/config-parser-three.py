#!/usr/bin/python3
from configparser import ConfigParser

parser = ConfigParser()
parser.read('sample_configuration.ini')

for candidate in ['session', 'class', 'city', 'ematter']:
    print('{:<12}: {}'.format(
        candidate, parser.has_section(candidate)))

