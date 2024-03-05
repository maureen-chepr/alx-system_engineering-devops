#!/usr/bin/python3
""" function that queries the Reddit API """
import pprint
import requests

BASE_URL = 'http://reddit.com/r/{}/hot.json'


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the titles of all hot articles"""
    headers = {'User-agent': 'CustomClient/1.0 (by /u/Mundane_Strategy7626)'}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return hot_list
    response = requests.get(BASE_URL.format(subreddit),
                            headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = "STOP"
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return recurse(subreddit, hot_list, after)
