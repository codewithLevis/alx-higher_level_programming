#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import select, create_engine, asc
from sys import argv
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    uri = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(uri, pool_pre_ping=True)
    conn = engine.connect()
    query = select(State.name, City.id, City.name).select_from(
            State).join(City).order_by(asc(State.id))
    result = conn.execute(query).fetchall()

    for state_name, city_id, city_name in result:
        print(f'{state_name}: ({city_id}) {city_name}')
    conn.close()
