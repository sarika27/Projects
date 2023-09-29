# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:51:33 2023

@author: N Vikas
"""

#insert into table

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "yourusername",
    passwd = "yourpassword"
    database ="mydatabase")
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("john", "highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")