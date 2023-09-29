# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:26:02 2023

@author: N Vikas
"""

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "yourusername",
    passwd = "yourpassword"
    )
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)