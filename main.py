# main.py

from scrape_reddit import get_reddit_user_content
from generate_persona import generate_persona

def main():
    reddit_url = input("Enter Reddit Profile URL: ").strip()
    if not reddit_url.startswith("https://www.reddit.com/user/"):
        print("Invalid URL")
        return

    username = reddit_url.split("/")[-2]  # Extract username
    print(f"Fetching posts for {username}...")

    reddit_data = get_reddit_user_content(username)
    
    # Prepare readable text for LLM
    formatted_data = "\n\n".join([
        f"Post Title: {p['title']}\nText: {p['selftext']}\nSubreddit: {p['subreddit']}" 
        for p in reddit_data["posts"]
    ] + [
        f"Comment: {c['body']}\nSubreddit: {c['subreddit']}\nLink: {c['link']}" 
        for c in reddit_data["comments"]
    ])

    print("Generating user persona...")
    persona_text = generate_persona(formatted_data, username)

    with open(f"{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(persona_text)

    print(f"Persona saved to {username}_persona.txt")

if __name__ == "__main__":
    main()
