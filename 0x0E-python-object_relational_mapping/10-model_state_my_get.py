#!/usr/bin/python3
# a script that prints the State object with the name passed as argument from
# the database hbtn_0e_6_usa

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

    query = session.query(State).order_by(State.id)
    if query:
        for line in query:
            if line.name == sys.argv[4]:
                print("{}".format(line.id))
    else:
        print("Not found")
