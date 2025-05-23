import praw
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
client_id = "NaOWHJF7Mb0dtvHR8zT9lQ"
client_secret = "D0zwHowYTW2Y9KQgqtYgxKidUt5S4w"

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent="thread-analyzer"
)

def fetch_reddit_thread(url):
    submission = reddit.submission(url=url)
    submission.comments.replace_more(limit=0)

    thread = {
        "title": submission.title,
        "body": submission.selftext,
        "url": url,
        "comments": []
    }

    def process_comment(comment):
        return {
            "body": comment.body,
            "score": comment.score,
            "replies": [process_comment(reply) for reply in comment.replies]
        }

    for top_level_comment in submission.comments:
        thread["comments"].append(process_comment(top_level_comment))

    return thread
