#!/usr/bin/python3
""" This module is for printing the State object
with the name passed as argument from the database hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import create_engine
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

    updated_state = session.query(State).filter(State.id == 2).first()
    if updated_state:
        updated_state.name = "New Mexico"
        session.commit()
    session.close()
