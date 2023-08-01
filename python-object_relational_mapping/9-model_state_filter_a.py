#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if all three arguments are provided (username, password, database name)
    if len(sys.argv) != 4:
        # Print the usage message and exit with an error code of 1
        print("Usage: python script_name.py <username> <password> <db_name>")
        sys.exit(1)

    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all State objects containing the letter 'a' and display them
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
