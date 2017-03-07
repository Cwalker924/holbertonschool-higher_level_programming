#!/usr/bin/python3
# a script that prints the first State object from the database hbtn_0e_6_usa
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    sesh = sessionmaker(bind=engine)
    session = sesh()

    query = session.query(State)
    trigger = 0
    if query:
        for data in query:
            if trigger < 1:
                print("{}: {}".format(data.id, data.name))
                trigger += 1
    else:
        print("Nothing")
