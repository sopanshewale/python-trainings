#!/usr/bin/python3

# Create a set.
items = {"arrow", "spear", "arrow", "arrow", "rock"}

print (type(items))
print(items)
print(len(items))

if "rock" in items:
    print("Rock exists")

if "clock" not in items:
    print("Cloak not found")

