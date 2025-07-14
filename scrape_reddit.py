import os
import praw
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

def get_reddit_user_content(username, limit=50):
    user = reddit.redditor(username)
    posts = []
    comments = []

    for post in user.submissions.new(limit=limit):
        posts.append({
            "title": post.title,
            "selftext": post.selftext,
            "url": post.url,
            "subreddit": str(post.subreddit)
        })

    for comment in user.comments.new(limit=limit):
        comments.append({
            "body": comment.body,
            "subreddit": str(comment.subreddit),
            "link": f"https://reddit.com{comment.permalink}"
        })

    return {"posts": posts, "comments": comments}
