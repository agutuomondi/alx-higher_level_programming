#!/bin/bash
#Send a request to the URL
curl -so /dev/null -w "%{http_code}" "$1"
