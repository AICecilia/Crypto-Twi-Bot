import requests
from config import TWITTER_COOKIES
from generate_tweet import generate_tweet_from_data

def auto_reply_to_comment(comment_id):
    reply_text = "Thanks!"  
    reply_content = generate_tweet_from_data([{'content': reply_text}])

    if reply_content:
        url = f"https://api.twitter.com/2/tweets/{comment_id}/replies"
        
        headers = {
            'Authorization': f"Bearer {TWITTER_COOKIES['auth_token']}",
            'Content-Type': 'application/json',
            'x-csrf-token': TWITTER_COOKIES['ct0'],
        }

        payload = {
            "status": reply_content
        }

        try:
            response = requests.post(url, json=payload, headers=headers, cookies=TWITTER_COOKIES)
            response.raise_for_status()
            print(f"Replied to comment: {comment_id}")
        except requests.exceptions.RequestException as e:
            print(f"Error replying to comment: {e}")
