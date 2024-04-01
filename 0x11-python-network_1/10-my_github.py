#!/usr/bin/python3

import sys
from requests import get, auth



if __name__ == "__main__":

    url = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    r = get(url, auth=auth.HTTPBasicAuth(user, password))

    print(r.json().get('id'))
