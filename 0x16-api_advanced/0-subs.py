#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            subscribers = data['data']['subscribers']
            return f"existing subreddit: {subscribers}"
        else:
            # If the subreddit data doesn't contain subscriber information
            return "existing subreddit"
    elif response.status_code == 404:
        # If the subreddit doesn't exist
        return "nonexisting subreddit"
    else:
        # If the request was unsuccessful, return 0
        return "unknown error"

