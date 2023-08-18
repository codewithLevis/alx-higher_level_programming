#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
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

if __name__ == '__main__':
    db = MySQLdb.connect(**arguments)
    cursor = db.cursor()
    cursor.execute("""
            SELECT cities.id, cities.name, states.name FROM cities
            INNER JOIN states ON cities.state_id = states.id
            ORDER BY cities.id
            """)
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
