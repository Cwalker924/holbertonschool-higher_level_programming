#!/usr/bin/python3
# a script that changes the name of a State object from the database
# hbtn_0e_6_usa

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    sesh = sessionmaker()
    session = sesh(bind=engine)

    query = session.query(State).filter(State.id == 2)

    for line in query:
        line.name = "New Mexico"
        session.commit()
        print("{}: {}".format(line.id, line.name))
