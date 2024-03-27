#!/bin/bash
# Check if the number of arguments !=2
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
