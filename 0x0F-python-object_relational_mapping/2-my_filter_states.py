#!/usr/bin/python3
"""
should displays all values in the states table where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    mySQLdb = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], mySQLdb=argv[3], charset="utf8")
    currsor = mySQLdb.cursor()
    currsor.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
                    id ASC".format(argv[4]))
    rows = currsor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    currsor.close()
    mySQLdb.close()
