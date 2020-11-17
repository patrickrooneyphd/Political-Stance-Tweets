import json
import os
import pandas as pd
import datetime
from accounts import *


def load_tweets(file):
    with open(file, 'r') as f:
        tweets = (json.loads(line) for i, line in enumerate(f.readlines()))
    return tweets


# Select attributes needed
data = {'created_at': [], 'tweet_id': [], 'tweet_id_str': [], 'full_text': [], 'display_text_range': [],
        'retweet': [], 'retweet_user_name': [], 'media': [],
        'user_id': [], 'user_id_str': [], 'user_name': [], 'user_screen_name': [], 'company': [],
        'user_followers_count': [], 'user_friends_count': [], 'user_num_favorited_tweets': [],
        'user_statuses_count': [], 'user_listed_count': [],
        'user_join_date': [], 'retweet_count': [], 'favorite_count': [], 'time_scraped': []}

output_dir = os.path.join(os.getcwd() + '/data/')
os.chdir(output_dir)
file_name = 'test_tweets.json'

tweets = load_tweets(file_name)

for t in tweets:                 # Try to iterate over keys k of data dict after first run.
    rt_media = False
    data['created_at'].append(t['created_at'])
    data['tweet_id'].append(t['id'])
    data['tweet_id_str'].append(t['id_str'])
    data['full_text'].append(t['full_text'])
    data['display_text_range'].append(t['display_text_range'])
    if 'retweeted_status' not in t.keys():
        data['retweet'].append(0)
        data['retweet_user_name'].append(None)
    else:
        data['retweet'].append(1)
        data['retweet_user_name'].append(t['retweeted_status']['user']['name'])
        if 'media' in t['retweeted_status']['entities'].keys():
            data['media'].append(1)
            rt_media = True
    if 'media' in t['entities'].keys() and not rt_media:
        data['media'].append(1)
    elif 'media' not in t['entities'].keys() and not rt_media:
        data['media'].append(0)
    data['user_id'].append(t['user']['id'])
    data['user_id_str'].append(t['user']['id_str'])
    data['user_name'].append(t['user']['name'])
    data['user_screen_name'].append(t['user']['screen_name'])
    if t['user']['screen_name'] in ceos.keys():
        company = ceos.get(t['user']['screen_name'])
        data['company'].append(company)
    else:
        company = None
        data['company'].append(company)
    data['user_followers_count'].append(t['user']['followers_count'])
    data['user_friends_count'].append(t['user']['friends_count'])
    data['user_num_favorited_tweets'].append(t['user']['favourites_count'])
    data['user_statuses_count'].append(t['user']['statuses_count'])
    data['user_listed_count'].append(t['user']['listed_count'])
    data['user_join_date'].append(t['user']['created_at'])
    data['retweet_count'].append(t['retweet_count'])
    data['favorite_count'].append(t['favorite_count'])
    data['time_scraped'].append(datetime.datetime.utcnow())


df = pd.DataFrame(data)
df['created_at'] = pd.to_datetime(df['created_at'])
df['user_join_date'] = pd.to_datetime(df['user_join_date'])
df.sort_values(by='created_at')

df.to_csv('test_tweets.csv')

print('Done converting json to df')
print('.CSV saved')

