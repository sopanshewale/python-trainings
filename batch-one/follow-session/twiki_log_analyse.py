#!/usr/bin/python3
import pandas as pd
import datetime as dt


twiki = pd.read_csv("TWiki_Application.log", delimiter="|")
print (twiki.head())

twiki.columns = ['junk1', 'time_stamp', 'username', 'action', 'topic', 'browser', 'ipaddress', 'junk2']
print (twiki.head())

twiki = twiki.drop('junk1', 1)
twiki = twiki.drop('junk2', 1)
print (twiki.head())

# converting '2017-01-01 - 07:01:48' to proper date
twiki['datetime'] = twiki['time_stamp'].apply(lambda x: dt.datetime.strptime(x,' %Y-%m-%d - %H:%M:%S '))
print (twiki.head(5))

# selecting data between two datetime

mask = (twiki['datetime']>'2017-01-30') & (twiki['datetime'] <= '2017-01-31')

print (twiki.loc[mask])

