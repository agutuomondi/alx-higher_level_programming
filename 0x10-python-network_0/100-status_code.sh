#!/bin/bash
curl -so /dev/null -w "%{http_code}" "$1"
