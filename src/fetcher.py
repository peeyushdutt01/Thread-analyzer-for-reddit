import praw
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Reddit API
reddit = praw.Reddit(
    client_id = st.secrets["REDDIT_CLIENT_ID"],
    client_secret = st.secrets["REDDIT_CLIENT_SECRET"],
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
