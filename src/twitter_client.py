import os
import time
from tweepy import Client
from tweepy.errors import TooManyRequests
from src.logger import logger

def initialize_twitter_client():
    return Client(
        consumer_key=os.getenv("TWITTER_API_KEY"),
        consumer_secret=os.getenv("TWITTER_API_SECRET_KEY"),
        access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
        access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    )

def post_tweet(client, tweet_content):
    try:
        response = client.create_tweet(text=tweet_content)
        logger.info(f"Tweet posted successfully: {tweet_content}")
        return response
    except TooManyRequests:
        
        reset_time = client.rate_limit_status()['resources']['statuses']['/statuses/update']['reset']
        wait_seconds = reset_time - time.time()
        logger.warning(f"Rate limit exceeded. Waiting for {wait_seconds / 60:.2f} minutes.")
        time.sleep(wait_seconds)
        post_tweet(client, tweet_content)
    except Exception as e:
        logger.error(f"Error posting tweet: {e}")
