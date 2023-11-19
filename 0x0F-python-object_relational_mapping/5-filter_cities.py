#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa based on
the given State name
"""
import sys
import MySQLdb


if __name__ == "__main__":
    """
    Extract MySQL credentials and databases name from cmd line args
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    """
    Connect to the MySQL server
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    """
    Create a cursor to interact with the database
    """
    cursor = db.cursor()

    """
    SQL query to retrieve cities of the fiven state
    """
    query = "SELECT cities.name FROM cities\
      JOIN states ON cities.state_id = states.id\
      WHERE states.name = %s\
      ORDER BY cities.id"

    """
    Execute the query with the state name as parameter
    """
    cursor.execute(query, (state_name,))

    """
    Fetch all the results
    """
    results = cursor.fetchall()

    """
    Format cities into a comma-separated string
    """
    print(", ".join([row[0] for row in results]))

    """
    Close cursor and database connection
    """
    cursor.close()
    db.close()
