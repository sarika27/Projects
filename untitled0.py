# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:02:35 2023

@author: N Vikas
"""

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "yourusername",
    passwd = "yourpassword"
    )
print(mydb)