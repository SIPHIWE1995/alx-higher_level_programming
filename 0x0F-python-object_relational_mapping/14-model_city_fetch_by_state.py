#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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
    Create a Session instance
    """
    session = Session()

    """
    Query the db to retrieve all City obj
    """
    cities = session.query(City, State).join(State).order_by(City.id).all()

    """
    Display the results
    """
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    """
    Close the session
    """
    session.close()
