import requests
from config import TWITTER_COOKIES
from generate_tweet import generate_tweet_from_data

def comment_on_tweet(user_id):

    url = f"https://api.twitter.com/2/tweets?user_id={user_id}&count=1"
    headers = {
        'Authorization': f'Bearer {TWITTER_COOKIES["auth_token"]}',
    }

    try:
        response = requests.get(url, headers=headers, cookies=TWITTER_COOKIES)
        response.raise_for_status()
        tweet = response.json()['data'][0]

        comment_text = generate_tweet_from_data([{'content': tweet['text']}])

        comment_url = f"https://api.twitter.com/2/tweets/{tweet['id']}/replies"
        comment_payload = {
            "status": comment_text
        }
        comment_response = requests.post(comment_url, json=comment_payload, headers=headers, cookies=TWITTER_COOKIES)
        comment_response.raise_for_status()
        print(f"Commented on tweet: {tweet['id']}")

    except requests.exceptions.RequestException as e:
        print(f"Error commenting on tweet: {e}")
