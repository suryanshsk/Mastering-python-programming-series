import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)

# Post a tweet
api.update_status('Hello, world! This is an automated tweet.')
