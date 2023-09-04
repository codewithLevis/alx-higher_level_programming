#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
use the package requests
"""
import requests

if __name__ == '__main__':
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print(f"Body response:\n\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
    response.close()
