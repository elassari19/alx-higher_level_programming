#!/usr/bin/python3
"""
should displays all values in the states table where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    dbcursor = db.cursor()
    dbcursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
                    id ASC".format(argv[4]))
    rows = dbcursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    dbcursor.close()
    db.close()
