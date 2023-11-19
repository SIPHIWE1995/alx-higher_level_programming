#!/usr/bin/python3
"""
Prints the State object with the name passed as arg
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Get MySQL credentials, db name, and state name from cmd line
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

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
    Query the db to retrieve the State object with the given name
    """
    state = session.query(State).filter(State.name == state_name).first()

    """
    Display the results or "Not found"
    """
    if state is not None:
        print(state.id)
    else:
        print("Not found")

    """
    Close the session
    """
    session.close()
