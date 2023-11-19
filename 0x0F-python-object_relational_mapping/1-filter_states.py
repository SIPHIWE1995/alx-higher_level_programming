#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' (upper N)
"""
import MySQLdb
import sys

if __name__ == "__main__":

    """
    Get MySQL credentials from the cmd line args
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
    Execute the SQL query to retrieve states starting with 'N'
    """
    query = "SELECT * FROM `states` WHERE name LIKE BINARY 'N%' ORDER BY `id`"
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
