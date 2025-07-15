# Reddit User Persona Generator 🧠

It scrapes a Reddit user’s posts/comments and generates a structured user persona using Gemini 2.0 Flash.

---

## 🔧 Features

- ✅ Scrapes recent Reddit posts and comments from a given user
- ✅ Uses Google Gemini 2.0 Flash Lite to generate a psychological persona
- ✅ Outputs results in a structured `.txt` file
- ✅ Includes citations linking persona traits to original Reddit content

---

## 📦 Installation

### 1. Clone or download the repo

```
git clone https://github.com/DiptarajSinha/reddit-scraper
cd <root-project-directory>
```
### 2. Install dependencies
```
pip install -r requirements.txt
```
### 3. Setup .env
Create a .env file in the root folder:
```
REDDIT_CLIENT_ID=your_id_here
REDDIT_CLIENT_SECRET=your_secret_here
REDDIT_USER_AGENT=user-persona-script by /u/yourusername
GEMINI_API_KEY=your_gemini_api_key
```

## 🚀 Usage
### Run the program:
```
python main.py
Enter a Reddit user profile URL: https://www.reddit.com/user/Hungry-Move-6603/
```
It will generate a file like: `Hungry-Move-6603_persona.txt`

### Example Output
See ```Hungry-Move-6603_persona.txt``` for a complete sample persona generated from real Reddit data.

## 🤖 Tech Stack
- Python
- Reddit API via praw
- Gemini 2.0 Flash Lite (via google-generativeai)

---
