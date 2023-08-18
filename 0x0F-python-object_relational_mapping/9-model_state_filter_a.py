#!/usr/bin/python3
"""
script that lists all State objects with letter a
fromthe database hbtn_0e_6_usa
"""
from sqlalchemy import select, create_engine, asc
from sys import argv
from model_state import Base, State


if __name__ == '__main__':
    uri = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(uri, pool_pre_ping=True)
    conn = engine.connect()
    query = select(State).where(State.name.like('%a%')).order_by(asc(State.id))
    result = conn.execute(query).fetchall()

    for id, name in result:
        print(f'{id}: {name}')
    conn.close()
