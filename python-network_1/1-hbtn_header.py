#!/usr/bin/python3
"""
This module sends a request to a given URL and prints the value of the
X-Request-Id header from the HTTP response.
"""

import sys
import urllib.request


def display_request_id():
    """
    Sends a request to the URL provided as a command-line argument and
    prints the X-Request-Id value from the response headers.
    """
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.headers
        request_id = headers.get("X-Request-Id")
        print(request_id)


if __name__ == "__main__":
    display_request_id()
