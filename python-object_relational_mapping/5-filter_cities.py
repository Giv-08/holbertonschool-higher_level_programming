#!/usr/bin/python3
""" This module is for taking in the name of a state as an argument
and lists all cities of that state"""

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

    state_name = sys.argv[4]
    cursor = db_connection.cursor()
    sql = "SELECT cities.name FROM cities JOIN states " \
        "ON cities.state_id = states.id WHERE states.name = %s" \
        "ORDER BY cities.id ASC"
    cursor.execute(sql, (state_name,))
    n_cities = cursor.fetchall()

    print(", ".join(n[0] for n in n_cities))
    cursor.close()
    db_connection.close()
