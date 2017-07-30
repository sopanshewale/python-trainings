#!/usr/bin/python3

a_set = set(range(10))
print (a_set)


squares = {x ** 2 for x in a_set}
print (squares) 

evens = {x for x in a_set if x % 2 == 0}
print (evens)


two_powers = {2**x for x in range(10)} 
print (two_powers)


