from transformers import GPT2LMHeadModel, GPT2Tokenizer

def auto_reply(client, model, tokenizer):
    recent_mentions = client.get_users_mentions(client.get_me().data.id)
    if recent_mentions.data:
        for mention in recent_mentions.data:
            prompt = f"Reply to a cryptocurrency comment: {mention.text}"
            reply_content = generate_tweet(model, tokenizer, prompt)
            try:
                client.create_tweet(
                    text=f"@{mention.author_id} {reply_content} #AIReply",
                    in_reply_to_tweet_id=mention.id
                )
                print(f"Reply sent: {reply_content}")
            except Exception as e:
                print(f"Auto-reply failed: {e}")
