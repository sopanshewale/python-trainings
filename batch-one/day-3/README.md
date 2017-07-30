# snippet one

```
f = None
for i in range (5):
   with open ('data.txt', 'r') as f:
        if i > 2: 
            break;
print (f.closed)

```
# snippet two 

```
for i in range(5):
    with open ('data.txt', 'w', encoding='utf-8') as f:
        f.write("Number: ", i)
 
with open('data.txt', 'r', encoding='utf-8') as fr:
    print(fr.read()) 
```

# snippet three

more data.txt
1
2

more t.py 

f = open('data.txt', 'r'):
for i in [100, 200]:
    f.readline()

for i in [100, 200]:
    print (f.readline())
```
# snippet four

```
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

```

# snippet five 

```
import time 
def foo():
   try:
      raise Exception("I know python!")
   except:
      time.sleep(10)
      return 1
   finally:
      return 2

k = foo()
print (k)

```
# snippet six

```
def printMax(a, b):
   if a > b:
      print (a, " is maximum")
   elif a == b:
      print (a, " is equal to ", b)
   else: 
      print (b, " is maximum")

printMax(3, 4)

```

# snippet seven

```

def func(a, b=5, c=10):
    print ('a is ', a' 'b is ', b, 'c is ', c)
    
func(3, 7)
func(25, c=24)
func(c=50, a = 100)

```

# snippet eight 

```
import configparser
import sys

parser = configparser.ConfigParser()

parser.add_section('name')
parser.set('first', 'Hari')
parser.set('last', 'Sadu')
parser.write(sys.stdout)


```

