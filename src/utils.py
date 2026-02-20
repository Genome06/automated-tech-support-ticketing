import re
import string

def preprocess_text(text):
    # Example of a preprocessing function that used in Week 1 & 2
    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    return text