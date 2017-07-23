#!/usr/bin/python3
# We can use "range", lists with append functionality. 

number = int (input ("Enter the Number: "))

expected_list = []
for n in  range(1, number+1):
   tmp = []
   num = n + 1
   for i in range(num):
       if i != 0:
            if n % i  == 0:
                tmp.append(i) 
   expected_list.append(tmp)

#junk = expected_list.pop()
#expected_list.insert(0, [1])
expected_list.insert(0, [])
print(expected_list)
