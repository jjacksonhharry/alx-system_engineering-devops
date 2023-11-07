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
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    response = requests.get(
            'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit),
            headers=headers)

    if response.status_code == 200 and
    response.json().get('kind') == 'Listing':
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)
