#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


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
    cursor.execute("""
            SELECT cities.name FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name LIKE BINARY '{}'
            ORDER BY cities.id
            """.format(sys.argv[4]))

    print(', '.join(city[0] for city in cursor.fetchall()))
    cursor.close()
    db.close()
