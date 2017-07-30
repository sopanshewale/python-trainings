#!/usr/bin/python3
from configparser import ConfigParser

try: 
   parser = ConfigParser()
   parser.read('sample_configuration.ini')
except configparser.ParsingError as err: 
   print('Could not parse:', err) 
   
version = parser.getfloat('session', 'version')
print (type(version))

# similarly we can have methods:
#    getboolean
#    getint 


