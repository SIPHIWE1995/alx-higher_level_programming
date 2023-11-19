#!/usr/bin/python3
"""
Adds the state object "Louisiana" to the database hbtn_0e_6_usa
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
    Create a new State object "Louisiana"
    """
    new_state = State(name="Louisiana")

    """
    Add the new State object to the session
    """
    session.add(new_state)

    """
    Commit the session to add the new State object to the database
    """
    session.commit()

    """
    Display the new states.id after creation
    """
    print(new_state.id)

    """
    Close the session
    """
    session.close()
