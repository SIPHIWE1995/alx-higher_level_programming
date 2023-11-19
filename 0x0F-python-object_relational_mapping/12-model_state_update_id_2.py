#!/usr/bin/python3
"""
Changes the name of a State object from the db hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    Get MySQL credentials and db name from cmd line args
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """
    Create a connection to the MySQL server
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
    Query the db to find the State object with id = 2
    """
    state_to_update = session.query(State).filter_by(id=2).first()

    """
    Update the name of the State object
    """
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    """
    Close the session
    """
    session.close()
