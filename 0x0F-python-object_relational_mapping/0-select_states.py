#!/usr/bin/python3
"""
should lists all states from the database
Your script should take 3 arguments
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    mySQLdb = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], mySQLdb=argv[3], charset="utf8")
    currsor = mySQLdb.cursor()
    currsor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = currsor.fetchall()
    for row in rows:
        print(row)
    currsor.close()
    mySQLdb.close()
