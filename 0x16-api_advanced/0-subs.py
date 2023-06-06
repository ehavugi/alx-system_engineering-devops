#!/usr/bin/python3
"""Module for number of reddit subscribers.
"""
import requests

def number_of_subscribers(subreddit):
    """ subReddit subscriber number
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}  # Set a User-Agent header to avoid 429 rate limit errors
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            # print(data['data'].keys())
            # print(data.get("after", "None"))
            subscribers = data["data"]["subscribers"]
            return subscribers
        except KeyError:
            # Invalid subreddit or JSON response structure changed
            return 0
    else:
        # Invalid subreddit or other request error
        return 0
