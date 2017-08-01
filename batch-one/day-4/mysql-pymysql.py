#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","welcome123","mysql" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : {} ".format( data))

# disconnect from server
db.close()

