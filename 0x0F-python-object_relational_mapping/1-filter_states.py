#!/usr/bin/python3
"""
script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
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
if __name__ == '__main__':
    db = MySQLdb.connect(**parameters)
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM states
            WHERE states.name LIKE BINARY "N%"
            ORDER BY states.id''')

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
