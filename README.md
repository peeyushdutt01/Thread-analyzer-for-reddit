
# 🧵 Reddit Thread Sentiment Analyzer

Reddit Thread Sentiment Analyzer is an interactive web application built with Streamlit that analyzes the sentiment of Reddit thread comments. It fetches a full Reddit discussion thread via the Reddit API (`praw`), processes each comment using the VADER sentiment analysis tool from `nltk`, and visualizes the emotional tone of the conversation.

The app helps users understand how discussions evolve across a thread — showing sentiment changes over comment depth, extracting the main discussion topics using `KeyBERT`, and generating a word cloud from all user comments. This is particularly useful for researchers, moderators, content creators, or anyone curious about online community dynamics.

Whether you're investigating controversial topics, exploring public opinion, or just want to visualize a conversation in a new way, this tool gives you a deep dive into Reddit's unique thread structure and sentiment flow.

---

## 📷 Reddit Thread Screenshot

![image](https://github.com/user-attachments/assets/759392b5-d31e-463c-8af9-5d4375314544)

🔗 [View the Reddit Thread](https://www.reddit.com/r/movies/comments/1jue18p/china_mulling_ban_on_hollywood_film_releases_in/)

---

## 🎬 Streamlit App Demo

![NLP-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/9867279c-3d31-4f6f-93ad-22ba376b3b2a)

---

## 🚀 Features

- Fetch threads and all comments using Reddit's API (`praw`)
- Sentiment analysis with VADER (NLTK)
- Extract top key discussion points with `KeyBERT`
- Word cloud visualization using `WordCloud`
- Comment sentiment depth chart using `matplotlib`
- Simple UI with `Streamlit`

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
````
git clone https://github.com/peeyushdutt01/Thread-analyzer-for-reddit.git
cd Thread-analyzer-for-reddit
````

### 2. Create a Virtual Environment 
````
python -m venv venv
venv\Scripts\activate
````

### 3. Install dependencies 
````
pip install -r requirements.txt
````

### 4. Add Reddit API Credentials
````
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
````

### 5. Run the app
````
streamlit run src/app.py
````



## 📂 Project Structure

src/
│
├── app.py              # Streamlit app (UI layer) <br>
├── fetcher.py          # Reddit thread fetching logic <br>
├── sentiment.py        # Sentiment analysis using NLTK VADER <br>
├── keypoints.py        # Key discussion point extraction using KeyBERT <br>
├── visualizer.py       # Word cloud and sentiment trend plots <br>
