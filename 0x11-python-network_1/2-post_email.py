#!/usr/bin/python3
"""
Python script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
body of the response (decoded in utf-8)
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = f"email={sys.argv[2]}".encode('ascii')
    request = urllib.request.Request(url, data=data)

    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode())
    except Exception:
        pass
