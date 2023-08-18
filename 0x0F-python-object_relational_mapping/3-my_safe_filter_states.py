#!/usr/bin/python3
"""
script that takes in an argument and displays all
values in the states table of
hbtn_0e_0_usa where name matches the argument
Protects Sql Injection
"""
import MySQLdb
from sys import argv


arguments = {
        'host': 'localhost',
        'user': argv[1],
        'passwd': argv[2],
        'db': argv[3],
        'port': 3306
        }

db = MySQLdb.connect(**arguments)
cursor = db.cursor()
cursor.execute('''
            SELECT * FROM states
            WHERE states.name LIKE BINARY "{}"
            ORDER BY states.id'''.format(argv[4]))
for row in cursor.fetchall():
    print(row)

cursor.close()
db.close()
