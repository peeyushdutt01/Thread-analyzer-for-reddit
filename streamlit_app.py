# src/app.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
import streamlit as st
from fetcher import fetch_reddit_thread
from sentiment import analyze_thread_sentiment
from keypoints import extract_keypoints
from visualizer import plot_sentiment_trend_fig, generate_wordcloud_fig

st.set_page_config(page_title="Reddit Thread Analyzer", layout="wide")
st.title("📊 Reddit Thread Analyzer")

url = st.text_input("Enter Reddit thread URL:", placeholder="https://www.reddit.com/r/...")

if url:
    with st.spinner("Fetching thread..."):
        thread = fetch_reddit_thread(url)

    st.subheader("🔍 Thread Title")
    st.markdown(f"**{thread['title']}**")

    with st.spinner("Analyzing sentiment..."):
        thread, avg_sentiment = analyze_thread_sentiment(thread)

    st.metric("Average Sentiment Score", f"{avg_sentiment:.3f}")

    st.subheader("📈 Sentiment Trend")
    st.pyplot(plot_sentiment_trend_fig(thread))

    st.subheader("🌟 Key Discussion Points")
    keypoints = extract_keypoints(thread)
    for kp in keypoints:
        st.markdown(f"**{kp['topic']}**")
        for ex in kp["examples"]:
            st.markdown(f"- {ex}")

    st.subheader("☁️ Word Cloud")
    st.pyplot(generate_wordcloud_fig(thread))
