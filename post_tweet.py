import requests
from config import TWITTER_COOKIES
from generate_tweet import generate_tweet_from_data

def post_tweet():
    tweets = load_cecilia_data('Crypto-Twi-Bot/data/cecilia_hsueh_tweets.json')

    tweet_content = generate_tweet_from_data(tweets)

    if tweet_content:
        url = "https://api.twitter.com/2/tweets"
        headers = {
            'Authorization': f'Bearer {TWITTER_COOKIES["auth_token"]}',
            'Content-Type': 'application/json'
        }

        payload = {
            "status": tweet_content
        }

        try:
            response = requests.post(url, json=payload, headers=headers, cookies=TWITTER_COOKIES)
            response.raise_for_status()
            print("Tweet posted successfully!")
        except requests.exceptions.RequestException as e:
            print(f"Error posting tweet: {e}")
