#!/usr/bin/python3

import configparser
import sys

parser = configparser.ConfigParser()

parser.add_section('bug_tracker')
parser.set('bug_tracker', 'url', 'http://example.com/bugs')
parser.set('bug_tracker', 'username', 'dhellmann')
parser.set('bug_tracker', 'password', 'secret')
#parser.write(sys.stdout)

f = open('myconfig.ini', 'w')
parser.write(f)
f.close()

