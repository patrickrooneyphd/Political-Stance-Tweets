#
# f100_tweets_gfloyd.py
#
# Author: Patrick Rooney
# Desc: Scrapes all tweets from Fortune 100 CEOs and company accounts in two week window before and after
# George Floyd killing in Minneapolis (May 25, 2020).
#
# Code Ref: https://github.com/bear/python-twitter/commit/090ff41234c5629391b0615e9bce56bc9d76a8e8

"""
Downloads all tweets from a given user.
Uses twitter.Api.GetUserTimeline to retrieve the last 3,200 tweets from a user.
Twitter doesn't allow retrieving more tweets than this through the API, so we get
as many as possible.
keys.py should contain the imported variables.
"""

# Test with Tim Cook (@tim_cook) and Jeff Bezos (@JeffBezos) in list.

from __future__ import print_function

import json
import sys

import twitter
from keys import ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET


def get_tweets(api=None, screen_name=None):
    timeline = api.GetUserTimeline(screen_name=screen_name, count=200)
    earliest_tweet = min(timeline, key=lambda x: x.id).id
    print("getting tweets before:", earliest_tweet)

    while True:
        tweets = api.GetUserTimeline(
            screen_name=screen_name, max_id=earliest_tweet, count=200
        )
        new_earliest = min(tweets, key=lambda x: x.id).id

        if not tweets or new_earliest == earliest_tweet:
            break
        else:
            earliest_tweet = new_earliest
            print("getting tweets before:", earliest_tweet)
            timeline += tweets

    return timeline


if __name__ == "__main__":
    api = twitter.Api(
        CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
    )
    screen_name = sys.argv[1]
    print(screen_name)
    timeline = get_tweets(api=api, screen_name=screen_name)

    with open('data/cook_bezos_example.json', 'w+') as f:
        for tweet in timeline:
            f.write(json.dumps(tweet._json))
            f.write('\n')
