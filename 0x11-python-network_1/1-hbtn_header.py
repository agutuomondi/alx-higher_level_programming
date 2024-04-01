#!/usr/bin/python3

"""Displays X-Request-Id header variable of request to given URL.
Usage: ./1-hbtn_header.py <URL>
"""

import urllib.request

import sys

if __name__ == "__main__":

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:

        header = response.info()

        print(header['X-Request-Id'])
