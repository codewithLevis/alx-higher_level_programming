#!/usr/bin/python3
"""
script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == '__main__':
    parameters = {
            'host': 'localhost',
            'user': sys.argv[1],
            'passwd': sys.argv[2],
            'db': sys.argv[3],
            'port': 3306
            }
    db = MySQLdb.connect(**parameters)
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM states
            WHERE states.name LIKE BINARY "N%"
            ORDER BY states.id''')

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
