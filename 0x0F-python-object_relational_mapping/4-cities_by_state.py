#!/usr/bin/python3
"""
should lists all cities from the database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    mySQLdb = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], mySQLdb=argv[3], charset="utf8")
    currsor = mySQLdb.cursor()
    currsor.execute("SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON cities.state_id = states.id ORDER BY cities.id")
    rows = currsor.fetchall()
    for row in rows:
        print(row)
    currsor.close()
    mySQLdb.close()
