#!/usr/bin/python3
""" This module is for filtering states starts witn 'n' using MySQLdb"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    cursor = db_connection.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        )
    n_states = cursor.fetchall()

    for n in n_states:
        print(n)

    db_connection.close()
