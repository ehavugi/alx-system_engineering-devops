#!/usr/bin/python3
"""
Recursively find all hot topics from a subredit and
return a list
"""
import requests


def count_words(subreddit, word_list,  hot_list=[], after=None, words={}):
    """Recursively find all hot topics from a subredit
    """
    if len(word_list) == 0:
        return None
    # print(word_list, words)
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    if after:
        headers["after"] = after
        response = requests.get(url + "?after=" + after,
                                headers=headers, allow_redirects=False)
    else:
        response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            after = data['data'].get('after', None)
            for i in data['data']['children']:
                datai = i['data']['title']
                hot_list.append(datai)
                for x in datai.split(" "):
                    for y in word_list:
                        y = y.replace("'", "").replace('"', "")

                        if x.lower().strip() == y.lower().strip():
                            words[y.lower()] = words.get(y.lower(), 0) + 1
                        # print(x.lower(), y.lower())

            if after:
                count_words(subreddit, word_list,
                            hot_list=hot_list, after=after, words=words)
                return hot_list
            wordsKeys = sorted(words.items(),
                               key=lambda kv: kv[1], reverse=True)
            for key in wordsKeys:
                print("{}: {}".format(key[0], key[1]))
            return None
        except Exception as e:
            return None
    else:
        # Invalid subreddit
        return None
