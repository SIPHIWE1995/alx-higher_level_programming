#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from
the databases hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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
    Query the db to retrieve State obj containing 'a'
    """
    states_with_a = session.query(State).filter(State.name.contains('a'))\
                           .order_by(State.id).all()

    """
    Display the results
    """
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    """
    Close the session
    """
    session.close()
