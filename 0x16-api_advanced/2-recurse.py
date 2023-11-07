#!/usr/bin/python3
"""
function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    queries the Reddit API and returns a list containing
    the titles of all hot articles
    """

    if after is None and len(hot_list) > 0:
        return hot_list
    # Recursive case: fetch the next page and append the titles to the list
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'api_advanced-project'}
    params = {"limit": 100, "after": after}
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            title = child.get("data").get("title")
            hot_list.append(title)
        return recurse(subreddit, hot_list, after)
    else:
        return None
