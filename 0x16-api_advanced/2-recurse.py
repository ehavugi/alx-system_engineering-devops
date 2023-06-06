#!/usr/bin/python3
"""
Recursively find all hot topics from a subredit and
return a list
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively find all hot topics from a subredit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    if after:
        headers["after"] = after
        response = requests.get(url + "?after=" + after, headers=headers)
    else:
        response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            after = data['data'].get('after', None)
            for i in data['data']['children']:
                hot_list.append(i['data']['title'])
            if after:
                recurse(subreddit, hot_list=hot_list, after=after)
                return hot_list
            return hot_list
        except Exception as e:
            return None
    else:
        # Invalid subreddit
        return None
