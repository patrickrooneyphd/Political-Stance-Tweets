#
# f100_tweets_gfloyd.py
#
# Author: Patrick Rooney
# Desc: Scrapes all tweets from Fortune 100 CEOs and company accounts in three week window before and after
# George Floyd killing in Minneapolis (May 25, 2020).
#
# Code Ref: https://www.kdnuggets.com/2016/06/mining-twitter-data-python-part-1.html

"""
Downloads all tweets from a given user.
Uses twitter.Api.GetUserTimeline to retrieve the last set of tweets from a user.
keys.py should contain the imported variables.
"""


from __future__ import print_function

import json
import os

import tweepy
import datetime
from keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from accounts import *

# Creating the authentication object:
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# Setting your access token and secret
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Creating the API object while passing in the auth information
api = tweepy.API(auth)

# Base Case: Get Date.Time and Tweets from one account.
usernames = list(ceos.keys())
start_date = datetime.datetime(2020, 5, 4, 0, 0, 0)
end_date = datetime.datetime(2020, 6, 15, 0, 0, 0)

tweets = []
file_name = 'test_tweets.json'
output_dir = os.path.join(os.getcwd() + '/data/')
os.chdir(output_dir)
output = open(file_name, "w")

for username in usernames:
    tmpTweets = api.user_timeline(username, tweet_mode='extended')  # Get all tweets from user timeline
    for tweet in tmpTweets:
        if tweet.created_at < end_date and tweet.created_at > start_date:
            tweets.append(tweet)

    while tmpTweets[-1].created_at > start_date:
        tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id, tweet_mode='extended')  # Find the id of tweet
        for tweet in tmpTweets:
            if tweet.created_at < end_date and tweet.created_at > start_date:
                output.write(json.dumps(tweet._json) + '\n')
    print('Finished ' + username)
output.close()

print('Done scraping')
