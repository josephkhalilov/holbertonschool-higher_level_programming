#!/usr/bin/python3
"""
This module sends a POST request to a given URL with an email parameter
and displays the body of the response.
"""

import sys
import requests


def post_email():
    """
    Sends a POST request to the URL provided as a command-line argument
    with the email parameter, then prints the response body.
    """
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}

    response = requests.post(url, data=data)
    print(response.text)


if __name__ == "__main__":
    post_email()
