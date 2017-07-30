
# write to file
with open('test.log', mode='w', encoding='utf-8') as a_file:
    a_file.write("This is Python Class")

# Verify
with open('test.log', mode='r', encoding='utf-8') as a_file:
    print (a_file.read())

# Let us try append 
with open('test.log', mode='a', encoding='utf-8') as a_file:
    a_file.write("This is Seriously Python Class")


# Verify
with open('test.log', mode='r', encoding='utf-8') as a_file:
    print (a_file.read())


 
