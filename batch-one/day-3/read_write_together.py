#!/usr/bin/python3

f = open('readandwrite.txt', 'r+')

f.write("Hello")
r = f.read()
f.write("Hello")
f.write("Hello")
print (r)

f.close()

