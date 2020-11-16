#
# f100_tweets_gfloyd.py
#
# Author: Patrick Rooney
# Desc: Scrapes all tweets from Fortune 100 CEOs and company accounts in three week window before and after
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
# Current setup is to add the names in the CLI,

from __future__ import print_function

import os
import pandas as pd

import tweepy
import datetime
from keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
# from account import *

# Creating the authentication object:
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# Setting your access token and secret
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Creating the API object while passing in the auth information
api = tweepy.API(auth)

# Base Case: Get Date.Time and Tweets from one account.
username = 'tim_cook'
start_date = datetime.datetime(2020, 5, 4, 0, 0, 0)
end_date = datetime.datetime(2020, 6, 15, 0, 0, 0)

tweets = []

tmpTweets = api.user_timeline(username, tweet_mode='extended')  # Get all tweets from user timeline
for tweet in tmpTweets:
    if tweet.created_at < end_date and tweet.created_at > start_date:
        tweets.append(tweet)

while tmpTweets[-1].created_at > start_date:
    tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id, tweet_mode='extended')  # Find the id of tweet
    for tweet in tmpTweets:
        if tweet.created_at < end_date and tweet.created_at > start_date:
            tweets.append(tweet)

tweets_df = pd.DataFrame(vars(tweets[i]) for i in range(len(tweets)))

# Select relevant columns
cols = ['_json', 'created_at', 'id', 'id_str', 'full_text', 'display_text_range', 'entities', 'source', 'user',
        'retweet_count', 'favorite_count', 'quoted_status_id', 'quoted_status']
tweets_df = tweets_df[cols]

# Export the df to csv in data directory
print(os.getcwd())

output_file = 'cook_tweets.csv'
output_dir = os.path.join(os.getcwd() + '/data/')
os.makedirs(output_dir, exist_ok=True)

tweets_df.to_csv(os.path.join(output_dir + output_file))


