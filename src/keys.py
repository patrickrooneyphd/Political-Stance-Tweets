#
# keys.py
#
# Desc: Accesses keys for access to the Twitter API, which are stored in .env file
#
# To replicate data collection, you need to apply for Twitter API access for an app, and generate
# authentication tokens under App --> Keys and Tokens --> Authentication Tokens (Access Tokens & Secret)
# --> Generate. These tokens are "TWTR_ACCESS_TOKEN" and "TWTR_ACCESS_TOKEN_SECRET", respectively.
#

from decouple import config

'''
.ENV Variables:

NOTE! The first two keys below are labelled "consumer keys" in the python-twitter docs. 
I follow this nomenclature.

TWTR_API_KEY: Your key is like your username. It is used to verify who you are to Twitter.
TWTR_SECRET_API_KEY: Your secret key is used like a password. It identifies your account. Keep this safe!
TWTR_BEARER_TOKEN: An access token used in authentication that allows you to pull specific data.
TWTR_ACCESS_TOKEN: An access token used in authentication that allows you to pull specific data.
TWTR_ACCESS_TOKEN_SECRET: An access token used in authentication that allows you to pull specific data.
'''

# To access local env variables in .env file...
# e.g.,
# API_USERNAME = config('USER')  # Insert the name of .env variable here
# API_KEY = config('KEY')

CONSUMER_KEY = config('TWTR_API_KEY')
CONSUMER_SECRET = config('TWTR_SECRET_API_KEY')
ACCESS_TOKEN_KEY = config('TWTR_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = config('TWTR_ACCESS_TOKEN_SECRET')


