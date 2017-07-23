# Quiz Code:

```
#!/usr/bin/python3
presidents = ['Clinton', 'Barack', 'Trump']
for president in presidents:
   if president == 'Trump':
        print ("No more Trump - please")
        break
   print ("Great - President: ", president)
else: 
   print ("I am so glad - even Trump was covered")

print ("I am done")

````
Another Code


```

#!/usr/bin/python3

ch = True
while (ch):
   key = input("Enter Key: ")
   print ("You entered: ", key)
   if key == 'Q':
       ch = False
       print ("Oh - you entered Q, you are making exit")


```


Another one

```
#!/usr/bin/python3

names1 = ['Amir', 'Sharukh', 'Chales', 'Dao']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
     if ls[0] == 'Alice':
          sum += 1
     if ls[1] == 'Bob':
          sum += 10

print (sum)
 

```

```

#!/usr/bin/python3

confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1] += 1

sum = 0
for k in confusion:
    sum += confusion[k]

print(sum)

```

```
confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1.0] = 4

sum = 0
for k in confusion:
    sum += confusion[k]

print(sum)

```

