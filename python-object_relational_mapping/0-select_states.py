#!/usr/bin/python3

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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    db_connection.close()
