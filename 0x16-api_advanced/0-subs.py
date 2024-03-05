#!/usr/bin/python3
"""
    function that queries the Reddit API and
    returns the number of subscribers
"""
import json
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and
    returns the number of subscribers
    """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {'User-Agent': 'maureen-chepr'}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get("data")
        if data:
            return data.get("subscribers", 0)
        else:
            return 0
    except json.JSONDecodeError:
        return 0
