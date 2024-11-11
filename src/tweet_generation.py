import json
import random
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from src.logger import logger

def initialize_gpt2_model():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = tokenizer.pad_token_id
    return model, tokenizer

def load_tweet_data(json_path):
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            tweet_data = json.load(f)
        return tweet_data
    except FileNotFoundError:
        logger.error(f"JSON file {json_path} not found.")
        return []

def generate_tweet(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(
        inputs['input_ids'],
        attention_mask=inputs['attention_mask'],
        max_length=280,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        temperature=0.8,
        top_p=0.9,
        top_k=50,
        do_sample=True
    )
    generated_tweet = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    logger.info("Generated tweet content: " + generated_tweet)
    return generated_tweet
