import json
import pandas as pd
import datetime
from accounts import *


def load_tweets(file):
    with open(file, 'r') as f:
        tweets = (json.loads(line) for i, line in enumerate(f.readlines()))
    return tweets


# Select attributes needed
data = {'created_at': [], 'tweet_id': [], 'tweet_id_str': [], 'full_text': [], 'tweet_length': [],
        'retweet': [], 'retweet_user_name': [], 'media': [], 'hashtags': [], 'retweet_count': [], 'favorite_count': [],
        'user_id': [], 'user_id_str': [], 'user_name': [], 'user_screen_name': [], 'company': [],
        'user_followers_count': [], 'user_friends_count': [], 'user_num_favorited_tweets': [],
        'user_statuses_count': [], 'user_listed_count': [], 'user_join_date': [], 'time_scraped': []
        }

data_labels = {'created_at': 'created_at', 'tweet_id': 'id', 'tweet_id_str': 'id_str',
               'full_text': 'full_text', 'retweet_count': 'retweet_count',
               'favorite_count': 'favorite_count'
               }

data_labels_user = {'user_id': 'id', 'user_id_str': 'id_str', 'user_name': 'name', 'user_screen_name': 'screen_name',
                    'user_followers_count': 'followers_count', 'user_friends_count': 'friends_count',
                    'user_num_favorited_tweets': 'favourites_count', 'user_statuses_count': 'statuses_count',
                    'user_listed_count': 'listed_count', 'user_join_date': 'created_at'
                    }

file_name = 'test_tweets.json'

tweets = load_tweets(file_name)

for t in tweets:                 # Try to iterate over keys k of data dict after first run.
    rt_media = False
    data['time_scraped'].append(datetime.datetime.utcnow())
    if t['user']['screen_name'] in ceos.keys():
        company = ceos.get(t['user']['screen_name'])
        data['company'].append(company)
    else:
        company = None
        data['company'].append(company)
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
    if t['entities']['hashtags']:
        tags = []
        for h in range(0, len(t['entities']['hashtags'])):
            tags.append(t['entities']['hashtags'][h]['text'])
        tag_str = ",".join(tags)
        data['hashtags'].append(tag_str)
    else:
        data['hashtags'].append(None)

    data['tweet_length'].append(t['display_text_range'][1])

    for key, value in data_labels.items():
        data[key].append(t[value])

    for k, v in data_labels_user.items():
        data[k].append(t['user'][v])

df = pd.DataFrame(data)
df['created_at'] = pd.to_datetime(df['created_at'])
df['user_join_date'] = pd.to_datetime(df['user_join_date'])
df.sort_values(by='created_at')

df.to_csv('test_tweets.csv')

print('Done converting json to df')
print('.CSV saved')


