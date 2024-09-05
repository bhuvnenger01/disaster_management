import tweepy
from config import Config

def get_twitter_data():
    # Twitter API authentication
    auth = tweepy.OAuthHandler(Config.TWITTER_API_KEY, Config.TWITTER_API_SECRET)
    api = tweepy.API(auth)
    
    # Example: Search for disaster-related tweets
    tweets = api.search(q="flood OR earthquake", lang="en", count=100)
    
    # Process the tweets and return the result
    tweet_data = [{"text": tweet.text, "user": tweet.user.screen_name} for tweet in tweets]
    
    return tweet_data
