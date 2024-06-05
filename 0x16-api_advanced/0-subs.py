#!/usr/bin/python3
"""Module to return the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-User-Agent"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(number_of_subscribers(sys.argv[1]))
    else:
        print("Please pass an argument for the subreddit to search.")
