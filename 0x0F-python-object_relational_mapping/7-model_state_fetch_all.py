#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    Get MySQL credentials and database name from the cmd line
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """
    Create the connection to the MySQL server
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (username, password, db_name))

    """
    Create a configured "Session" class
    """
    Session = sessionmaker(bind=engine)

    """
    Create a Session instance
    """
    session = Session()

    """
    Query the database to retrieve all State objects
    """
    states = session.query(State).order_by(State.id).all()

    """
    Display the results
    """
    for state in states:
        print("{}: {}".format(state.id, state.name))

    """
    Close the session
    """
    session.close()
