import asyncio
import random
from src.config import load_environment_variables
from src.twitter_client import initialize_twitter_client
from src.tweet_generation import initialize_gpt2_model
from src.scheduler import setup_scheduled_tasks, run_schedule
from src.logger import logger

if __name__ == "__main__":
    try:
        load_environment_variables()
        client = initialize_twitter_client()
        model, tokenizer = initialize_gpt2_model()

        json_path = "./data/cecilia_hsueh_tweets.json"
        setup_scheduled_tasks(client, model, tokenizer, json_path)

        logger.info("Starting Crypto-Twi-Bot with async scheduling...")
        asyncio.run(run_schedule())

    except ValueError as e:
        logger.error(f"Environment configuration error: {e}")
    except Exception as e:
        logger.error(f"An unknown error occurred during execution: {e}")
