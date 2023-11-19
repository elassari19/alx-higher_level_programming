#!/usr/bin/python3
"""
should lists all cities of that state based on the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    dbcursor = db.cursor()
    dbcursor.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (argv[4],))
    rows = dbcursor.fetchall()
    print(", ".join(city[0] for city in rows))
    dbcursor.close()
    db.close()
