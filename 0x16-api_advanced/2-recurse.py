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
        after_data = response.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = response.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
