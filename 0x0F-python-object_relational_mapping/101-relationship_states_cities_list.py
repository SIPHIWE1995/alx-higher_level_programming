#!/usr/bin/python3
"""
Lists all State objects and corresponding City
objects contained in the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State  # Import from relationship_state.py
from relationship_city import City


if __name__ == "__main__":
    """
    Get MySQL credentials and database name from cmd line args
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """
    Create the connection to the MySQL server
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           username, password, db_name))

    """
    Create a configured "Session" class
    """
    Session = sessionmaker(bind=engine)

    """
    Create a Session instance
    """
    session = Session()

    """
    Query the db to retrieve all State and City objects
    """
    states = session.query(State).order_by(State.id).all()

    """
    Display the results
    """
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    """
    Close the session
    """
    session.close()
