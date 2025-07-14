import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_persona(reddit_data, username):
    prompt = f"""
You are a helpful AI assistant that generates detailed user personas from Reddit activity.

Below is a Reddit user's activity. Your task is to create a detailed persona in the following format:

1. Name: (assume or keep as Reddit username)
2. Age (if guessed), Occupation (if mentioned), Location (if possible)
3. Traits (Practical, Active, etc.)
4. Motivations (Health, Career, etc.)
5. Personality (MBTI-style)
6. Behavior & Habits
7. Frustrations
8. Goals & Needs
9. Citation: For each attribute, include a quote or link to the Reddit post/comment you used.

Reddit Username: {username}
Posts & Comments:
{reddit_data}
"""

    response = model.generate_content(prompt)
    return response.text
