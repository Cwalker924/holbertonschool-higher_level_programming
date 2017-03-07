#!/usr/bin/python3
# a script that adds the State object "Louisiana" to the database hbtn_0e_6_usa

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

    add_state = State(name="Louisiana")
    session.add(add_state)
    session.commit()

    query = session.query(State).order_by(State.id).filter(
        State.name == "Louisiana")
    trigger = 0
    for line in query:
        print(line.id)
