#
# scrape_tweets.py
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

# Get CEOs and Corporate Accounts from accounts.py
usernames = list(combined_accounts.keys())

# Set start and end Dates three weeks before/after G. Floyd Shooting (May 25, 2020)
start_date = datetime.datetime(2020, 5, 4, 0, 0, 0)
end_date = datetime.datetime(2020, 6, 15, 0, 0, 0)

# Create objects for list of tweets, output file, account log file, output directory, open output file
tweets = []
file_name = 'test_tweets.json'
account_log_file = 'account_log.txt'
output_dir = os.path.join(os.getcwd() + '/data/')
os.chdir(output_dir)


# Load previously scraped tweets before rate-limit cutoff.
# Remove usernames from whom we've already scraped all relevant tweets.
account_log_read = open(account_log_file, 'r')
existing_tweets = account_log_read.read().splitlines()
print(existing_tweets)
for t in existing_tweets:
    if t in usernames:
        print("Already scraped", t, "... Removing from list.")
        usernames.remove(t)

# Scrape tweets around a certain date:
tweet_count = 0
for username in usernames:
    try:
        tmpTweets = api.user_timeline(username, tweet_mode='extended')  # Get all tweets from user timeline
        for tweet in tmpTweets:
            if tweet.created_at < end_date and tweet.created_at > start_date:
                tweets.append(tweet)
                print(tweets)
        while tmpTweets[-1].created_at > start_date:
            print('Scraping ' + username)
            tmpTweets = api.user_timeline(username, max_id=tmpTweets[-1].id, tweet_mode='extended')  # Find tweet id
            for tweet in tmpTweets:
                if tweet.created_at < end_date and tweet.created_at > start_date:
                    tweet_count += 1
                    output = open(file_name, "a")
                    output.write(json.dumps(tweet._json) + '\n')
                    print("Scraped tweets so far: ", tweet_count)
                    output.close()
        account_log = open(account_log_file, "a")
        account_log.write(username + '\n')
        account_log.close()
        print('Finished ' + username)

    except NameError:
        raise NameError(username + " account does not exist or is empty")

print('Done scraping')

