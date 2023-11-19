#!/usr/bin/python3
"""
Deles all State obj with a name containing the letter 'a'
from the database hbtn_0e_6_usa
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
    Create the connection to the MySQL server
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (username, password, db_name))

    """
    Create a configured "Session" class
    """
    Session = sessionmaker(bind=engine)

    """
    Create a session instance
    """
    session = Session()

    """
    Query the db to find State obj with 'a' in teir name
    """
    states_with_a = session.query(State).filter(State.name.contains('a')).all()

    """
    Delete the State obj
    """
    for state in states_with_a:
        session.delete(state)
    session.commit()

    """
    Close the session
    """
    session.close()
