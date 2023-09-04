#!/usr/bin/python3
"""
Python script that takes in a URL
sends a request to the URL and displays the body of the response
"""
import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode())
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.status}")
