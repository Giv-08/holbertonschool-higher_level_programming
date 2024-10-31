#!/usr/bin/python3
""" This module is for deletes all State objects with a
name containing the letter a from the database hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import create_engine, delete
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
        )

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    a_states = session.query(State).filter(State.name.like('%a%')).all()
    for a in a_states:
        session.delete(a)
    session.commit()
    session.close()
