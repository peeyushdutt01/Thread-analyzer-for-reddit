from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def get_sentiment_label(score):
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def analyze_comment_sentiment(text):
    score = sia.polarity_scores(text)
    compound = score["compound"]
    label = get_sentiment_label(compound)
    return compound, label

def analyze_thread_sentiment(thread_json):
    sentiment_scores = []

    def recurse(comment):
        score, label = analyze_comment_sentiment(comment["body"])
        comment["sentiment_score"] = score
        comment["sentiment_label"] = label
        sentiment_scores.append(score)

        for reply in comment.get("replies", []):
            recurse(reply)

    for c in thread_json["comments"]:
        recurse(c)

    average = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0
    return thread_json, average
