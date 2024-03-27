#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

size=$(curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r')

if [ -z "$size" ]; then
    size=$(curl -s "$1" | wc -c)
fi

echo "$size"
