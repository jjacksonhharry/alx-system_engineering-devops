#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        children = data.get("data", {}).get("children", [])

        if children:
            for post in children:
                post_data = post.get("data")
                if post_data:
                    print(post_data.get("title"))
        else:
            print("No posts found in the subreddit.")
    else:
        print("None")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
