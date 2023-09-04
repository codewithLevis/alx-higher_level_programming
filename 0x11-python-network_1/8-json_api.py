#!/usr/bin/python3
"""
a Python script that takes in a letter
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
import sys

if __name__ == '__main__':
    data = {'q': ""}
    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}

    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        data = response.json()
        if "id" in data and "name" in data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
