import requests
from config import TWITTER_COOKIES

def retweet(user_id):
    url = f"https://api.twitter.com/2/tweets?user_id={user_id}&count=1"
    headers = {
        'Authorization': f'Bearer {TWITTER_COOKIES["auth_token"]}',
    }

    try:
        response = requests.get(url, headers=headers, cookies=TWITTER_COOKIES)
        response.raise_for_status()
        tweet = response.json()['data'][0]

        retweet_url = f"https://api.twitter.com/2/tweets/{tweet['id']}/retweet"
        retweet_response = requests.post(retweet_url, headers=headers, cookies=TWITTER_COOKIES)
        retweet_response.raise_for_status()
        print(f"Retweeted tweet: {tweet['id']}")

    except requests.exceptions.RequestException as e:
        print(f"Error retweeting: {e}")
