#!/usr/bin/python3
""" prints all States object from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Creating a session.
    Session = sessionmaker(bind=engine)
    session = Session()

    # printing from database.
    for item in session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id):
        print("{}: {}".format(item.id, item.name))

    # close session
    session.close()
