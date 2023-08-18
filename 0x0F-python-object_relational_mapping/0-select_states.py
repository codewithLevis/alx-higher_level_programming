#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

parameters = {
        'host': 'localhost',
        'user': argv[1],
        'passwd': argv[2],
        'db': argv[3],
        'port': 3306
        }
db = MySQLdb.connect(**parameters)
cursor = db.cursor()
cursor.execute('SELECT * FROM states ORDER BY states.id;')
result = cursor.fetchall()

for i in result:
    print(i)

cursor.close()
db.close()
