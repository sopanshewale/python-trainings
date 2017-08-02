# snippet 1

```
CREATE TABLE presidents(
   id INT(11) NOT NULL AUTO_INCREMENT,
   name VARCHAR(45) NOT NULL,
   age int(11) NOT NULL,
   PRIMARY KEY (id)
   ) ENGINE=InnoDB;

```

# snippet 2

```
INSERT INTO presidents (id, name, age) VALUES (1, 'D Trump', 74);
INSERT INTO presidents (name, age) VALUES ('B. Obama', 55);

```

# snippet 3

```
sentence = 'the quick brown fox jumps over the lazy dog'
words = sentence.split()
words_lengths = [len(words) for word in words if word!="the"]
print (words_lengths)

```

# snippet 4

```
def writer():
    title = 'Sir'
    name = ([lambda x:title + ' ' + x)
    return name

who = writer()
who('Arthur')

```

# snippet 5

```
import re
import numpy as np
year = []
finish_time = []
with open("100m_running.csv", "r") as file:
    for line in file:
        line = re.sub("\s+", "", line)
        line_elements = line.split(",")
        if line_elements[0] != '':
             year.append(int(line_elements[0]))
        if line_elements[1] != '':
            finish_time.append(float(line_elements[1]))
# Here I have two lists. year & speed_time 
import matplotlib.pyplot as plt
plt.bar(year, finish_time)
plt.xlabel("Year")
plt.ylabel("Time - Finish")
plt.show()

```

# snippet 6

```
```

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1],[r'$-1$', r'$0$', r'$+1$'])
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")
plt.legend(loc='upper left', frameon=False)

plt.show()
```

# snippet 7
```

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1],[r'$-1$', r'$0$', r'$+1$'])
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")
plt.legend(loc='upper left', frameon=False)

plt.show()
```


# snippet 8 

```
plt.hist(finish_time, bins=5)
plt.show()
```

# snippet 9 


```
import datetime as dt
prices = []
dates = []
with open('GOOG.txt', "r") as f:
    for line in f:
        data = line.split(",")
        prices.append(data[1])
        day_y = data[0][0:4]
        day_m = data[0][4:6]
        day_d = data[0][6:8]
        dates.append(str(day_m) + '/' + str(day_d) + '/' + str(day_y))

days = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.xlabel("Trading Days")
plt.ylabel("Stock Price")
plt.plot(days,prices)
plt.gcf().autofmt_xdate()
plt.show()
```



# Random Walk 
* http://sphelps.net/teaching/random-walks-slides.html#/


```
>>> import pandas as pd
>>> s = pd.Series(['Usain Bolt', 9.63, 'Yohan Blake', 9.75, 'Justin Gatlin', 9.79])
>>> s
0       Usain Bolt
1             9.63
2      Yohan Blake
3             9.75
4    Justin Gatlin
5             9.79
dtype: object
>>> 

```
You can pass the index list:

```
>>> s = pd.Series(['Usain Bolt', 9.63, 'Yohan Blake', 9.75, 'Justin Gatlin', 9.79], index=['A', 'B', 'C', 'D', 'E', 'F'])
>>> s
A       Usain Bolt
B             9.63
C      Yohan Blake
D             9.75
E    Justin Gatlin
F             9.79
dtype: object
>>> 

```
You can also use dictionaries to create the series

```
>>> runners  =  {'Usain Bolt': 9.63, 'Yohan Blake': 9.75, 'Justin Gatlin': 9.79}
>>> runners
{'Yohan Blake': 9.75, 'Usain Bolt': 9.63, 'Justin Gatlin': 9.79}
>>> r = pd.Series(runners)
>>> r
Justin Gatlin    9.79
Usain Bolt       9.63
Yohan Blake      9.75
dtype: float64
>>> 

```
Accessing Elements

```

>>> r[['Yohan Blake', 'Yohan Blake']]
Yohan Blake    9.75
Yohan Blake    9.75
dtype: float64
>>> 
>>> r[['Yohan Blake', 'Usain Bolt']]
Yohan Blake    9.75
Usain Bolt     9.63
dtype: float64
>>> 

```

Look at other ways to access more elements

```
>>> runners  =  {'Usain Bolt': 9.63, 'Yohan Blake': 9.75, 'Justin Gatlin': 9.79, 'Tyson Gay': 9.8, 'Ryan Bailey': 9.88, 'Churandy Martina': 9.94, 'Richard Thompson': 9.98, 'Asafa Powell': 11.99}
>>> 
>>> r = pd.Series(runners)
>>> r
Asafa Powell        11.99
Churandy Martina     9.94
Justin Gatlin        9.79
Richard Thompson     9.98
Ryan Bailey          9.88
Tyson Gay            9.80
Usain Bolt           9.63
Yohan Blake          9.75
dtype: float64
>>> r[r>10]
Asafa Powell    11.99
dtype: float64
>>> r[r<9.8]
Justin Gatlin    9.79
Usain Bolt       9.63
Yohan Blake      9.75
dtype: float64
>>> 

```
Operations on the fly 
```

>>> r[['Superman']]
Superman   NaN
dtype: float64
>>> r['Superman']=5.0
>>> r['Batman'] = 6.0
>>> r
Asafa Powell        11.99
Churandy Martina     9.94
Justin Gatlin        9.79
Richard Thompson     9.98
Ryan Bailey          9.88
Tyson Gay            9.80
Usain Bolt           9.63
Yohan Blake          9.75
Superman             5.00
Batman               6.00
dtype: float64
>>> r[r<9] = 1.0
>>> r
Asafa Powell        11.99
Churandy Martina     9.94
Justin Gatlin        9.79
Richard Thompson     9.98
Ryan Bailey          9.88
Tyson Gay            9.80
Usain Bolt           9.63
Yohan Blake          9.75
Superman             1.00
Batman               1.00
dtype: float64
>>> print ('Ironman' in r)
False
>>> print ('Superman' in r)
True
>>> print ('Milkha Singh' in r)
False
>>> 

```

Addition of two Series 

```
>>> new_r = pd.Series({'Lalita Baber': 15.0,  'O P Jaisha': 16.0, 'Kavita Raut': 20.0, 'Usain Bolt':9.63,  'Milkha Singh':None})
>>> new_r.isnull()
Kavita Raut     False
Lalita Baber    False
Milkha Singh     True
O P Jaisha      False
Usain Bolt      False
dtype: bool
>>> new_r.notnull()
Kavita Raut      True
Lalita Baber     True
Milkha Singh    False
O P Jaisha       True
Usain Bolt       True
dtype: bool
>>> 

```

### Practice on Series

* For dictionary for High Protein Fruits
100gm 
```

Fruit,Protein,Fat,Calories,Carbs
Dried Apricots,3.39,0.51,241,62.64
Raisins,4.45,0.67,434,114.81
Guava,2.3,0.86,61,12.89
Dates,0.2,0.03,23,6.23
Avocado,4.02,29.47,322,17.15

```
 


## DataFrames

```
>>> data = {'name':['Usain Bolt','Yohan Blake','Justin Gatlin','Tyson Gay','Ryan Bailey','Churandy Martina','Richard Thompson','Asafa Powell'],
...         'speed':[9.63,9.75,9.79,9.8,9.88,9.94,9.98,11.99],
...         'height':[76.77,70.86,72.83,70.07,75.98,70.07,70.01,70.8],
...         'weight':[209.439,167.551,182.984,165.347,216.053,163.142,176.37,191.802]}
>>> 
>>> data
{'speed': [9.63, 9.75, 9.79, 9.8, 9.88, 9.94, 9.98, 11.99], 'name': ['Usain Bolt', 'Yohan Blake', 'Justin Gatlin', 'Tyson Gay', 'Ryan Bailey', 'Churandy Martina', 'Richard Thompson', 'Asafa Powell'], 'height': [76.77, 70.86, 72.83, 70.07, 75.98, 70.07, 70.01, 70.8], 'weight': [209.439, 167.551, 182.984, 165.347, 216.053, 163.142, 176.37, 191.802]}
>>> 

```

Reading from CSV File. 

```

>>> food = pd.read_csv("food.csv")
>>> food
                      Food  Index  Calories  Cholesterol  Total_Fat  Sodium  \
0          Frozen Broccoli      1      73.8          0.0        0.8    68.2   
1              Carrots,Raw      2      23.7          0.0        0.1    19.2   
2              Celery, Raw      3       6.4          0.0        0.1    34.8   
3              Frozen Corn      4      72.2          0.0        0.6     2.5   
4      Lettuce,Iceberg,Raw      5       2.6          0.0        0.0     1.8   
5      Peppers, Sweet, Raw      6      20.0          0.0        0.1     1.5   
6          Potatoes, Baked      7     171.5          0.0        0.2    15.2   
7                     Tofu      8      88.2          0.0        5.5     8.1   
8          Roasted Chicken      9     277.4        129.9       10.8   125.6   
9       Spaghetti W/ Sauce     10     358.2          0.0       12.3  1237.1   
10     Tomato,Red,Ripe,Raw     11      25.8          0.0        0.4    11.1   
11        Apple,Raw,W/Skin     12      81.4          0.0        0.5     0.0   
12                  Banana     13     104.9          0.0        0.5     1.1   
13                  Grapes     14      15.1          0.0        0.1     0.5   
14     Kiwifruit,Raw,Fresh     15      46.4          0.0        0.3     3.8   

```


```

>>> import pandas as pd
>>> raw_data = { 
...              'subject': ['1', '2', '3', '4', '5'],
...              'first_name': ['Michel', 'Mark', 'Matt', 'Ryan', 'Gary'],
...              'last_name': ['Phelps', 'Spitz', 'Biondi', 'Lochte', 'Hall']
...            }
>>> 
>>> raw_data
{'subject': ['1', '2', '3', '4', '5'], 'first_name': ['Michel', 'Mark', 'Matt', 'Ryan', 'Gary'], 'last_name': ['Phelps', 'Spitz', 'Biondi', 'Lochte', 'Hall']}
>>> df_a = pd.DataFrame(raw_data, columns = ['subject', 'first_name', 'last_name'])
>>> df_a
  subject first_name last_name
0       1     Michel    Phelps
1       2       Mark     Spitz
2       3       Matt    Biondi
3       4       Ryan    Lochte
4       5       Gary      Hall
>>> 


```


and second set

```

>>> raw_data = {
...             'subject': ['4', '5', '6', '7', '8', '9'],
...             'first_name': ['Ian', 'Aaron', 'Nathan', 'Tom', 'Don', 'Johny'],
...             'last_name': ['Thorpe', 'Peirsol', 'Adrian', 'Jager', 'Schollander', 'Weis'] 
...            }
>>> df_b = pd.DataFrame(raw_data, columns = ['subject', 'first_name', 'last_name'])
>>> df_b
  subject first_name    last_name
0       4        Ian       Thorpe
1       5      Aaron      Peirsol
2       6     Nathan       Adrian
3       7        Tom        Jager
4       8        Don  Schollander
5       9      Johny         Weis
>>> 


```


Third one 

```

>>> raw_data = {
...             'subject': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
...             'test'   : [51, 15, 15, 61, 16, 14, 15, 1, 61, 16] 
...            }
>>> df_n = pd.DataFrame(raw_data, columns = ['subject','test'])
>>> df_n
  subject  test
0       1    51
1       2    15
2       3    15
3       4    61
4       5    16
5       7    14
6       8    15
7       9     1
8      10    61
9      11    16
>>> 

```

Join dataframes on rows

```
>>> df_new = pd.concat([df_a, df_b])
>>> df_new
  subject first_name    last_name
0       1     Michel       Phelps
1       2       Mark        Spitz
2       3       Matt       Biondi
3       4       Ryan       Lochte
4       5       Gary         Hall
0       4        Ian       Thorpe
1       5      Aaron      Peirsol
2       6     Nathan       Adrian
3       7        Tom        Jager
4       8        Don  Schollander
5       9      Johny         Weis
>>> 

```

Join along axis

```
>>> pd.concat([df_a, df_b], axis=1)      
  subject first_name last_name subject first_name    last_name
0       1     Michel    Phelps       4        Ian       Thorpe
1       2       Mark     Spitz       5      Aaron      Peirsol
2       3       Matt    Biondi       6     Nathan       Adrian
3       4       Ryan    Lochte       7        Tom        Jager
4       5       Gary      Hall       8        Don  Schollander
5     NaN        NaN       NaN       9      Johny         Weis
>>> 

```

Merge 

```

>>> pd.merge(df_new, df_n, on='subject')
  subject first_name    last_name  test
0       1     Michel       Phelps    51
1       2       Mark        Spitz    15
2       3       Matt       Biondi    15
3       4       Ryan       Lochte    61
4       4        Ian       Thorpe    61
5       5       Gary         Hall    16
6       5      Aaron      Peirsol    16
7       7        Tom        Jager    14
8       8        Don  Schollander    15
9       9      Johny         Weis     1
>>> 

```


```
>>> pd.merge(df_new, df_n, left_on='subject', right_on='subject')
  subject first_name    last_name  test
0       1     Michel       Phelps    51
1       2       Mark        Spitz    15
2       3       Matt       Biondi    15
3       4       Ryan       Lochte    61
4       4        Ian       Thorpe    61
5       5       Gary         Hall    16
6       5      Aaron      Peirsol    16
7       7        Tom        Jager    14
8       8        Don  Schollander    15
9       9      Johny         Weis     1
>>> 

```

outer merge

```
>>> pd.merge(df_a, df_b, on='subject', how='outer')
  subject first_name_x last_name_x first_name_y  last_name_y
0       1       Michel      Phelps          NaN          NaN
1       2         Mark       Spitz          NaN          NaN
2       3         Matt      Biondi          NaN          NaN
3       4         Ryan      Lochte          Ian       Thorpe
4       5         Gary        Hall        Aaron      Peirsol
5       6          NaN         NaN       Nathan       Adrian
6       7          NaN         NaN          Tom        Jager
7       8          NaN         NaN          Don  Schollander
8       9          NaN         NaN        Johny         Weis
>>> 

```

Inner Join 

```
>>> pd.merge(df_a, df_b, on='subject', how='inner')
  subject first_name_x last_name_x first_name_y last_name_y
0       4         Ryan      Lochte          Ian      Thorpe
1       5         Gary        Hall        Aaron     Peirsol
>>> 

```


Left and Right joins


```
>>> pd.merge(df_a, df_b, on='subject', how='right')
  subject first_name_x last_name_x first_name_y  last_name_y
0       4         Ryan      Lochte          Ian       Thorpe
1       5         Gary        Hall        Aaron      Peirsol
2       6          NaN         NaN       Nathan       Adrian
3       7          NaN         NaN          Tom        Jager
4       8          NaN         NaN          Don  Schollander
5       9          NaN         NaN        Johny         Weis
>>> pd.merge(df_a, df_b, on='subject', how='left')
  subject first_name_x last_name_x first_name_y last_name_y
0       1       Michel      Phelps          NaN         NaN
1       2         Mark       Spitz          NaN         NaN
2       3         Matt      Biondi          NaN         NaN
3       4         Ryan      Lochte          Ian      Thorpe
4       5         Gary        Hall        Aaron     Peirsol
>>> 

```

On the basis of indexes

```
>>> pd.merge(df_a, df_b, right_index=True, left_index=True)
  subject_x first_name_x last_name_x subject_y first_name_y  last_name_y
0         1       Michel      Phelps         4          Ian       Thorpe
1         2         Mark       Spitz         5        Aaron      Peirsol
2         3         Matt      Biondi         6       Nathan       Adrian
3         4         Ryan      Lochte         7          Tom        Jager
4         5         Gary        Hall         8          Don  Schollander
>>> 

```

