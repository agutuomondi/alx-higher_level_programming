#!/usr/bin/python3

""" Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
#!/usr/bin/python3

import requests
import sys

def get_latest_commits(owner_name, repo_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        commits = response.json()[:10]  # Get the latest 10 commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to retrieve commits - {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <owner_name> <repo_name>")
        sys.exit(1)

    owner_name = sys.argv[1]
    repo_name = sys.argv[2]

    get_latest_commits(owner_name, repo_name)

