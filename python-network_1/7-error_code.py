
#!/usr/bin/python3
"""
This module sends a GET request to a URL and displays the body of the
response. If the HTTP status code is >= 400, it prints the error code.
"""

import sys
import requests


def fetch_url():
    """
    Sends a GET request to the URL provided as a command-line argument.
    Prints the response body if the status code is < 400, else prints
    'Error code:' followed by the HTTP status code.
    """
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    fetch_url()
