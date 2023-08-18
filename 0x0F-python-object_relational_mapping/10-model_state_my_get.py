#!/usr/bin/python3
"""
script that lists the first State objects from database hbtn_0e_6_usa
"""
from sqlalchemy import select, create_engine, asc
from sys import argv
from model_state import Base, State


if __name__ == '__main__':
    uri = "mysql+mysqldb://{}:{}@localhost/{}"
    engine = create_engine(uri.format(argv[1], argv[2], argv[3]))
    conn = engine.connect()
    query = select(State).where(State.name.like(
        f'{argv[4].split(";")[0]}')).order_by(asc(State.id))
    result = conn.execute(query).first()

    if result:
        print(f'{result[0]}')
    else:
        print('Not found')
    conn.close()
