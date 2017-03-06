#!/usr/bin/python3
# a script that takes in an argument and displays all values in the states table
# of hbtn_0e_0_usa where name matches the argument. But this time, one safe from
# MySQL injection!

import sys
import MySQLdb

usa_db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = usa_db.cursor()
cursor.execute("SELECT * From states ORDER BY id ASC;")
states = cursor.fetchall()

for state in states:
    if state[1] == sys.argv[4]:
        print(state)

cursor.close()
usa_db.close()
