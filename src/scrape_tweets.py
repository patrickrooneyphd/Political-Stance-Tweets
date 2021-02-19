#
# scrape_tweets.py
#
# Author: Patrick Rooney
# Desc: Scrapes all tweets from Fortune 100 CEOs and company accounts in three week window before and after
# George Floyd incident in Minneapolis (May 25, 2020).
#
# Code Ref: https://www.kdnuggets.com/2016/06/mining-twitter-data-python-part-1.html
#           https://medium.com/better-programming/how-to-scrape-tweets-with-snscrape-90124ed006af

import json
import os
import pandas as pd
import datetime
from accounts import *

json_file = 'tweets.json'
pkl_file = 'tweets_df_raw.pkl'
csv_file = 'tweets_df_raw.csv'

tweet_data = []

column_labels = ['date', 'tweet_id', 'text', 'replies', 'retweets', 'likes',
                 'quotes', 'media',
                 'source_label', 'username', 'ceo_account', 'compustat_company',
                 'user_join_date', 'user_followers', 'user_friends', 'user_statuses',
                 'user_favorites', 'user_listed', 'user_media',
                 ]


# Set start and end Dates three weeks before/after G. Floyd Incident (2020-05-04 to 2020-06-15)
# Add in CLI command for each username
# Create dictionary of usernames and username commands
def create_username_commands(out_file=json_file):
    """
    :param out_file: json file storing tweets
    :return: dictionary of CLI commands for scrape_data() function
    """
    usernames = list(combined_accounts.keys())  # Get CEOs and Corporate Accounts from accounts.py
    username_commands = []
    for username in usernames:
        username_commands.append("snscrape --jsonl --progress --since 2020-05-04 twitter-search "  
                                 "'from:"+username+" until:2020-06-15' >> "+out_file)

    username_dict = {usernames[i]: username_commands[i] for i in range(len(usernames))}
    return username_dict


# Change from source to data folder
def change_to_dir(ext='/data'):
    """
    :param ext: path extension to other file (must be one below root directory... e.g., src, data)
    :return: (none)
    """
    print('Current Working Directory: ' + os.getcwd())
    os.chdir('..')
    data_dir = os.path.join(os.getcwd() + ext)
    os.chdir(data_dir)
    print('Directory Changed')
    print('New Working Directory: ' + os.getcwd())


# Scrape data from Twitter using snscrape
def scrape_data():
    """
    :return: (none... CLI commands return tweet objects line by line to json file listed in
    create_username_commands())
    """
    for user, command in username_dict.items():
        try:
            print('Starting ' + user)
            # Scrape tweets for each user using the CLI command above
            os.system(command)
            print('Finished ' + user)

        except NameError:
            raise NameError(user + " account does not exist. Check name.")

    print('Done scraping')


# Load and read JSON tweets file
def load_tweets(load_file=json_file):
    """
    :param load_file: json file to load into memory
    :return: tweet objects
    """
    print('Loading tweets from: '+load_file)
    with open(load_file, 'r') as f:
        tweets = (json.loads(line) for i, line in enumerate(f.readlines()))
    return tweets


# Load JSON data into list of lists for DF
def json_to_df(load_file, out_file):
    """
    :param load_file: json file to load into memory
    :param out_file: file to store dataframe
    :return:
    """
    tweets = load_tweets(load_file)
    for t in tweets:
        if isinstance(t['media'], list):
            media = (t['media'][0]['type'])
        else:
            media = 'null'
        if t['user']['username'] in ceos.keys():
            ceo_account = 1
        else:
            ceo_account = 0
        tweet_data.append([t['date'], t['id'], t['content'], t['replyCount'], t['retweetCount'], t['likeCount'],
                           t['quoteCount'], media,
                           t['sourceLabel'], t['user']['username'], ceo_account,
                           combined_accounts[t['user']['username']],
                           t['user']['created'], t['user']['followersCount'], t['user']['friendsCount'],
                           t['user']['statusesCount'], t['user']['favouritesCount'], t['user']['listedCount'],
                           t['user']['mediaCount']
                           ])
    print('The length of the data is: ', len(tweet_data[0]))
    print('The length of the columns is: ', len(column_labels))
    df = pd.DataFrame(tweet_data, columns=column_labels)
    df.to_pickle('./' + out_file, protocol=4)
    df.to_csv('./' + csv_file)  # Also save to CSV
    print("Wrote dataframe to file: " + out_file)


if __name__ == '__main__':
    username_dict = create_username_commands()
    change_to_dir('/data')
    scrape_data()
    json_to_df(json_file, pkl_file)

