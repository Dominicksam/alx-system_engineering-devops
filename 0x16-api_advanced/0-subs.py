#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""


import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}  # Set a custom User-Agent to prevent Too Many Requests error
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            # If the subreddit data doesn't contain subscriber information
            return 0
    else:
        # If the request was unsuccessful, return 0
        return 0

