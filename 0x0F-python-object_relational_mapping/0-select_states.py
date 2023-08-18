#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
script should take 3 arguments:
mysql username, mysql password and database name
Usage: ./0-select_states.py root root hbtn_0e_0_usa
"""
import MySQLdb
import sys

parameters = {
        'host': 'localhost',
        'user': sys.argv[1],
        'passwd': sys.argv[2],
        'db': sys.argv[3],
        'port': 3306
        }
if __name__ == '__main__':
    db = MySQLdb.connect(**parameters)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY states.id;')
    result = cursor.fetchall()

    for i in result:
        print(i)

    cursor.close()
    db.close()
