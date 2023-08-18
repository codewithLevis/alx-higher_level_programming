#!/usr/bin/python3
"""
script that takes in an argument and displays all
values in the states table of
hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import sys


arguments = {
        'host': 'localhost',
        'user': sys.argv[1],
        'passwd': sys.argv[2],
        'db': sys.argv[3],
        'port': 3306
        }

if __name__ == '__main__':
    db = MySQLdb.connect(**arguments)
    cursor = db.cursor()
    cursor.execute('''
                SELECT * FROM states
                WHERE states.name LIKE BINARY "{}"
                ORDER BY states.id'''.format(sys.argv[4]))
    for row in cursor.fetchall():
        print(row)
