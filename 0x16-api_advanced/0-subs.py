#!/usr/bin/python3
"""
a script that returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    a function that returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code == 404:  # Subreddit not found
            return 0
        else:
            # Handle other status codes or potential errors
            return 0
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return 0
