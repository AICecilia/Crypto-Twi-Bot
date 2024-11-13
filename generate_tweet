import random
import google.generativeai as genai
import os
import json

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def load_cecilia_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_tweet_from_data(tweets):
    random_tweets = random.sample(tweets, 10)

    style_prompt = (
        "Generate a tweet about cryptocurrency, with a casual and thought-provoking tone. "
        "The content should be concise, direct, and somewhat motivational. "
        "Do not reference specific dates, events, or people. "
        "An example would be: '95 percent of people haven't tried crypto. Not because they don't want to. "
        "Because we never built for them.' It should have a reflective yet optimistic feeling."
    )

    prompt = f"{style_prompt} Based on the following content, generate a new tweet:\n"
    prompt += "\n".join([tweet['content'] for tweet in random_tweets])

    model = genai.GenerativeModel("gemini-1.5-flash")
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error generating tweet: {e}")
        return None
