#!/usr/bin/python3
# a script that lists all cities from the database hbtn_0e_4_usa

import sys
import MySQLdb

if __name__ == "__main__":
    usa_db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3], host="localhost", port=3306)
    cursor = usa_db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN  states ON cities.state_id = states.id ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    usa_db.close()
