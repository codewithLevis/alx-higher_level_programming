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
db = MySQLdb.connect(**arguments)
cursor = db.cursor()
cursor.execute("""
        SELECT cities.name FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE BINARY '{}'
        ORDER BY cities.id
        """.format(argv[4]))

print(', '.join(city[0] for city in cursor.fetchall()))
cursor.close()
db.close()
