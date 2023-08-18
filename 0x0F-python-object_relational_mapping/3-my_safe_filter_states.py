#!/usr/bin/python3
"""
script that takes in an argument and displays all
values in the states table of
hbtn_0e_0_usa where name matches the argument
Protects Sql Injection
"""
import MySQLdb
import sys


if __name__ == '__main__':
    arguments = {
            'host': 'localhost',
            'user': sys.argv[1],
            'passwd': sys.argv[2],
            'db': sys.argv[3],
            'port': 3306
            }
    db = MySQLdb.connect(**arguments)
    cursor = db.cursor()
    cursor.execute('''
                SELECT * FROM states
                WHERE states.name LIKE BINARY "{}"
                ORDER BY states.id'''.format(sys.argv[4].split(';')[0]))
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
