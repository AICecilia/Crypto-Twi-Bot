import time
import logging
from post_tweet import post_tweet
from retweet import retweet
from comment_on_tweet import comment_on_tweet
from auto_reply_to_comment import auto_reply_to_comment

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

def get_random_interval():
    # each hour 3-12 times
    times_per_hour = random.randint(3, 12)
    return 3600 / times_per_hour

def run_schedule():
    while True:
        try:
            log_info("Starting scheduled tasks")

            post_tweet()

            log_info("Retweeting user's tweet")
            retweet("target_user_id")

            log_info("Commenting on tweet and replying")
            comment_on_tweet("target_user_id")

            interval = get_random_interval()
            log_info(f"Waiting for {interval:.2f} seconds until next task")
            time.sleep(interval)
            
        except Exception as e:
            log_error(f"An error occurred: {str(e)}")

            time.sleep(60)


