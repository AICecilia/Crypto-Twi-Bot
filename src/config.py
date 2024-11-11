import os
from dotenv import load_dotenv

def load_environment_variables():
    load_dotenv()
    required_vars = [
        "TWITTER_API_KEY", "TWITTER_API_SECRET_KEY",
        "TWITTER_ACCESS_TOKEN", "TWITTER_ACCESS_TOKEN_SECRET"
    ]
    for var in required_vars:
        if not os.getenv(var):
            raise ValueError(f"Environment variable {var} is not set. Please check your .env file.")
    print("Environment variables loaded successfully.")
