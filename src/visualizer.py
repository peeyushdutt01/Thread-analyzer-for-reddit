# src/visualizer.py
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_sentiment_trend_fig(thread_json):
    sentiments = []

    def collect(comment, depth=0):
        sentiments.append((depth, comment["sentiment_score"]))
        for reply in comment.get("replies", []):
            collect(reply, depth + 1)

    for comment in thread_json["comments"]:
        collect(comment)

    depths = [d for d, _ in sentiments]
    scores = [s for _, s in sentiments]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(depths, scores, marker="o")
    ax.set_title("Sentiment Score by Comment Depth")
    ax.set_xlabel("Depth")
    ax.set_ylabel("Sentiment Score")
    ax.grid(True)
    return fig

def generate_wordcloud_fig(thread_json):
    text = " ".join([c["body"] for c in thread_json["comments"]])
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    return fig
