#!/usr/bin/python3

""" Python script takes URL and email address,
sends a POST request passed URL with email as parameter,
and displays body of response.
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""

import requests
import sys

def get_latest_commits(owner_name, repo_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)
    return response

def display_commits(response):
    if response.status_code == 200:
        commits = response.json()[:10]  # Get the latest 10 commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error: Failed to retrieve commits from the repository.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <owner_name> <repo_name>")
        sys.exit(1)

    owner_name = sys.argv[1]
    repo_name = sys.argv[2]

    response = get_latest_commits(owner_name, repo_name)
    display_commits(response)
