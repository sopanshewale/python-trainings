def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator()
print(mygenerator)
print(type(mygenerator))


#for i in mygenerator:
#    print (i)

print (next(mygenerator))
print (next(mygenerator))
print (next(mygenerator))

