#!/usr/bin/python3
# a script that lists all states with a name starting with N (upper N) from the
# database hbtn_0e_0_usa
import sys
import MySQLdb

if __name__ == "__main__":
    usa_db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3], host="localhost", port=3306)
    cursor = usa_db.cursor()
    cursor.execute("SELECT * From states ORDER BY id ASC;")
    states = cursor.fetchall()

    for state in states:
        if state[1][0] is "N":
            print(state)

    cursor.close()
    usa_db.close()
