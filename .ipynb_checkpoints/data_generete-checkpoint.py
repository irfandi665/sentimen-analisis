import tweepy

# Your app's bearer token can be found under the Authentication Tokens section
bearer_token = "AAAAAAAAAAAAAAAAAAAAAFmxjgEAAAAAcvzC8Cymvy5EBokzSnNvB6kG0eA%3DttyC7wewD0bYWZcnXb2NR449JAtimZ9ZRqGNuqqBqkpfwZ5Z85"

# Your app's API/consumer key and secret can be found under the Consumer Keys
consumer_key = 'LcftdwP6IJ9NODrGPguIapEuh'
consumer_secret = 'XF5I2CwcDHaxT9pvTYHpWH4M6EdH8JkvvJpmBDOedYpbnphXLR'

# Your account's (the app owner's account's) access token and secret for your
access_token = '1595635150804525056-aj6QvEK7kBN9DxlA0KYfp22RvgtQsY'
access_token_secret = 'PDzNrVfkvj3Twj7usfuLvnxwZlsvEpwOuMlxfKQ5xa74j'

# You can authenticate as your app with just your bearer token
#           client = tweepy.Client(bearer_token=bearer_token)

# You can provide the consumer key and secret with the access token and access
# token secret to authenticate as a user
#           client = tweepy.Client(
#               consumer_key=consumer_key, consumer_secret=consumer_secret,
#               access_token=access_token, access_token_secret=access_token_secret
#           )

client = tweepy.Client(bearer_token)

# Search Recent Tweets
# This endpoint/method returns Tweets from the last seven days

keyword = "tweepy"

# By default, this endpoint/method returns 10 results
# You can retrieve up to 100 Tweets by specifying max_results
response = client.search_recent_tweets(keyword, max_results=100, tweet_fields=["created_at", "lang"])

# The method returns a Response object, a named tuple with data, includes, errors, and meta fields
print(response.meta)

# In this case, the data field of the Response returned is a list of Tweet objects
tweets = response.data

# Each Tweet object has default ID and text fields
for tweet in tweets:
    print(tweet.id, tweet.lang, tweet.created_at, tweet.text)