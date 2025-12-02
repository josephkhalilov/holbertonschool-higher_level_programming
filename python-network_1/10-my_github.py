#!/usr/bin/python3
"""
This module uses the GitHub API with Basic Authentication to
display the authenticated user's id.
"""

import sys
import requests


def get_github_id():
    """
    Sends a GET request to the GitHub API using the username and
    personal access token (as password) provided via command-line
    arguments. Prints the user's id if authentication is successful,
    otherwise prints None.
    """
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, token))
    try:
        data = response.json()
        print(data.get("id"))
    except ValueError:
        print(None)


if __name__ == "__main__":
    get_github_id()
