#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    """
    Get MySQL credentials and database name from cmd line args
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """
    Connect to MySQL server
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    """
    Create a cursor object to interact with the database
    """
    cursor = db.cursor()

    """
    Construct and execute the SQL query
    """
    query = "SELECT cities.id, cities.name, states.name FROM cities\
      JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    cursor.execute(query)

    """
    Fetch all the results
    """
    results = cursor.fetchall()

    """
    Display the results
    """
    for row in results:
        print(row)

    """
    Close the cursor and database connection
    """
    cursor.close()
    db.close()
