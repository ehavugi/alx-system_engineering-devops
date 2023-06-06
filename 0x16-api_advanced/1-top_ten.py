#!/usr/bin/python3
"""
Top ten subreddit's hotest topics
"""
import requests


def top_ten(subreddit):
    """print top hotest topics on a subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            x = 0
            for i in data['data']['children']:
                if x < 10:
                    print(i['data']['title'])
                x += 1
            return 0
            print("None")
        except Exception as e:
            # return 0
            print("None", e)
    else:
        # Invalid subreddit or other request error
        print("None")
