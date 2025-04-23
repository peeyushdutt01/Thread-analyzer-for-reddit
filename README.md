
# 🧵 Reddit Thread Sentiment Analyzer

This project analyzes Reddit threads to determine the sentiment of comments using Natural Language Processing (NLP). It includes a Streamlit-based web app that lets users input a subreddit and visualize sentiment trends interactively.

---

## 📷 Reddit Thread Screenshot

![image](https://github.com/user-attachments/assets/759392b5-d31e-463c-8af9-5d4375314544)

🔗 [View the Reddit Thread](https://www.reddit.com/r/movies/comments/1jue18p/china_mulling_ban_on_hollywood_film_releases_in/)

---

## 🎬 Streamlit App Demo

![NLP-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/9867279c-3d31-4f6f-93ad-22ba376b3b2a)

---

## 🚀 Features

- Fetch Reddit threads using the Reddit API (via `praw`)
- Perform sentiment analysis on thread comments using VADER (from `nltk`)
- Visualize sentiment trends in a Streamlit app
- Easily configurable subreddit and post limit

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
├── app.py              # Streamlit app (UI layer)
├── fetcher.py          # Reddit thread fetching logic
├── sentiment.py        # Sentiment analysis using NLTK VADER
├── keypoints.py        # Key discussion point extraction using KeyBERT
├── visualizer.py       # Word cloud and sentiment trend plots
