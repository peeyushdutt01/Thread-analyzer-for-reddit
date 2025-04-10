from keybert import KeyBERT
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
kw_model = KeyBERT(model)

def extract_keypoints(thread_json, top_n=3):
    all_text = " ".join([comment["body"] for comment in thread_json["comments"]])
    keywords = kw_model.extract_keywords(all_text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=top_n)

    # Just return top N keywords and use them to find example comments
    keypoints = []
    for kw, _ in keywords:
        examples = [c["body"] for c in thread_json["comments"] if kw.lower() in c["body"].lower()]
        keypoints.append({
            "topic": kw,
            "examples": examples[:3]
        })

    return keypoints
