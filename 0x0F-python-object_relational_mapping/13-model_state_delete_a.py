#!/usr/bin/python3
"""
script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""
from sqlalchemy import delete, create_engine
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    uri = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(uri, pool_pre_ping=True)
    conn = engine.connect()
    query = delete(State).where(State.name.like('%a%'))
    result = conn.execute(query)
    conn.close()
