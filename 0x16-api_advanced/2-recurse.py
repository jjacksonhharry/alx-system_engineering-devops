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

    # Set a custom User-Agent header
    headers = {"User-Agent": "YourBot/1.0 (by YourUsername)"}

    # Build the URL for the subreddit's hot posts with pagination
    url =
    f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        data = response.json()
        children = data.get("data", {}).get("children", [])

        # Iterate through the posts and add their titles to the hot_list
        for post in children:
            post_data = post.get("data")
            if post_data and "title" in post_data:
                hot_list.append(post_data["title"])

        if data["data"]["after"]:
            return recurse(subreddit, hot_list, data["data"]["after"])
        else:
            return hot_list
    else:
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
