#!/usr/bin/python3

boxes = {}
jars = {}
crates = {}

boxes['cereal'] = 1
boxes['candy'] = 2
jars['honey'] = 4
crates['boxes'] = boxes
crates['jars'] = jars

print(len(crates[boxes]))

