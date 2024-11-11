import schedule
import asyncio
from src.twitter_client import post_tweet
from src.tweet_generation import generate_tweet, load_tweet_data
from src.auto_reply import auto_reply
from src.logger import logger

async def schedule_tweet(client, model, tokenizer, json_path):
    tweet_data = load_tweet_data(json_path)
    if not tweet_data:
        logger.warning("Tweet data is empty, skipping tweet.")
        return

    random_tweet = random.choice(tweet_data)
    prompt = f"{random_tweet.get('content', '')}"
    generated_tweet = generate_tweet(model, tokenizer, prompt)
    ai_generated_tweet = f"{generated_tweet} #AI #Cecilia"

    try:
        post_tweet(client, ai_generated_tweet)
        logger.info("Tweet posted successfully.")
    except Exception as e:
        logger.error(f"Failed to post tweet: {e}")

async def schedule_auto_reply(client, model, tokenizer):
    try:
        auto_reply(client, model, tokenizer)
        logger.info("Auto-reply completed successfully.")
    except Exception as e:
        logger.error(f"Auto-reply error: {e}")

async def run_schedule():
    while True:
        schedule.run_pending()
        await asyncio.sleep(60)  

def setup_scheduled_tasks(client, model, tokenizer, json_path):
    schedule.every(1).hour.do(lambda: asyncio.create_task(schedule_tweet(client, model, tokenizer, json_path)))
    schedule.every(10).minutes.do(lambda: asyncio.create_task(schedule_auto_reply(client, model, tokenizer)))
