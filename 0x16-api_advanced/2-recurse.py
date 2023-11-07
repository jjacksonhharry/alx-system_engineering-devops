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
    if hot_list is None:
        hot_list = []

    url = f
    "https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            for post in data["data"]["children"]:
                hot_list.append(post["data"]["title"])

            # Check if there are more posts to fetch
            if data["data"]["after"]:
                return recurse(subreddit, hot_list, data["data"]["after"])
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
