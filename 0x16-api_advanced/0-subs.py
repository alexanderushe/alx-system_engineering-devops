#!/usr/bin/python3

import requests
import sys

def number_of_subscribers(subreddit):
    # Construct the URL for the subreddit's API endpoint
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Reddit API'}
    
    # Send the GET request
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except KeyError:
            return 0  # Invalid subreddit format
    else:
        return 0  # Invalid subreddit or other error

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an arrgument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        try:
            subscribers = number_of_subscribers(subreddit)
        except Exception as e:
            print(e)
        else:
            print("{} has {:d} subscribers".format(subreddit,subscribers))
