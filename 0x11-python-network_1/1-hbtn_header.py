#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
displays the value of the X-Request-Id variable
found in the header of the response
"""
import urllib.request
import sys

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            id = response.headers.get("X-Request-Id")
            if id:
                print(id)
    except Exception:
        pass
