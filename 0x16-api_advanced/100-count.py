#!/usr/bin/python3
"""
function that queries the Reddit API, parses the title of all hot
articles, and prints a sortedcount of given keywords
(case-insensitive, delimited by spaces
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    function that queries the Reddit API, parses the title of all hot
    articles, and prints a sorted count of given keywords
    """
    if counts is None:
        counts = {}

    url = f
    "https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {"User-Agent": "YourBot/1.0 (by YourUsername)"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code != 200:
            return counts

        for post in data["data"]["children"]:
            title = post["data"]["title"].lower()
            for word in word_list:
                if f' {word} ' in f' {title} ':
                    counts[word] = counts.get(word, 0) + 1

        # Check if there are more posts to fetch
        if data["data"]["after"]:
            return count_words(subreddit,
                               word_list,
                               data["data"]["after"],
                               counts)
        else:
            sorted_counts = sorted(counts.items(),
                                   key=lambda item: (-item[1],
                                   item[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")

    except Exception as e:
        return counts


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print
        ("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [word.lower() for word in sys.argv[2].split()]
        count_words(subreddit, word_list)
