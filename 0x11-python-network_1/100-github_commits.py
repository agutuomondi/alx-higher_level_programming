#!/usr/bin/python3

""" Python script takes URL and email address,
sends a POST request passed URL with email as parameter,
and displays body of response.
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""

import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
