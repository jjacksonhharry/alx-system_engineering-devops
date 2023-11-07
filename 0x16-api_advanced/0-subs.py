#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    response = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers=headers)

    if response.status_code == 200 and response.json().get('kind') == 't5':
        return response.json().get('data').get('subscribers')
    else:
        return 0
