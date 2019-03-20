"""
resources used besides docs
https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library
will run every time computer is turned on
Task Scheduler library - twitter bot
"""
import tweepy
import credentials
import os

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)


"""
# finds a hashtag and prints the last 'n' many hashtags 
for tweet in tweepy.Cursor(api.search, q = '#existentialism').items(2):
    print(f'Tweet by: @ {tweet.user.screen_name}')
    print(f'{tweet.text}')
"""

# Tweet aka writes tweet to Twitter account
def write_tweet():
    import random_quote_generator

    tweet = random_quote_generator.string
    api.update_status(status=tweet)


write_tweet()