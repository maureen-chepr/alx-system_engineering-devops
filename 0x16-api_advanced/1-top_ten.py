#!/usr/bin/python3
import requests
"""
functions that queries the reddit api
"""


def top_ten(subreddit):
    """
    function that queries the Reddit API and
    prints the titles of the first 10 hot posts
    """
    url = "https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit)
    header = {'User-Agent': 'maureen-chepr/1.0'}
    req = requests.get(url, headers=header, allow_redirects=False)
    if req.status_code != 200:
        print(None)
        return
    req = req.json()
    if "data" in req:
        for post in req.get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)
