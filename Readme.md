# Crypto-Twi-Bot

Crypto-Twi-Bot is an automated Twitter bot that posts AI-generated thoughts about cryptocurrency. The content is based on a customized dataset to capture the style and tone relevant to the crypto theme.

## Setup Instructions

1. Clone the project:
    ```bash
    git clone https://github.com/AICecilia/Crypto-Twi-Bot.git
    cd Crypto-Twi-Bot
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure environment variables:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Insert your Twitter API keys in the `.env` file.

4. Run the project:
    ```bash
    python main.py
    ```

## Project Structure

- `main.py`: The main script to run the bot.
- `src/`: Contains modularized source code files.
- `data/cecilia_hsueh_tweets.json`: Example tweet dataset.
