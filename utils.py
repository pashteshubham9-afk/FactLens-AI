"""
utils.py

Shared helpers used by train.py, predict.py and app.py so all three
pieces treat input text exactly the same way.
"""

import re

# Common phrases that show up disproportionately in sensational / fake
# style writing. This is NOT the classifier - the machine learning model
# makes the actual prediction. This list is only used to show the user
# *why* something looks suspicious, as a transparent, explainable extra
# signal alongside the model's prediction.
RED_FLAG_PHRASES = [
    "you won't believe", "doctors hate", "one weird trick", "miracle cure",
    "secretly", "government is hiding", "government hiding", "banned",
    "share before", "before it's deleted", "before it gets deleted",
    "cures cancer", "cure cancer", "instantly cures", "cured overnight",
    "shocking video", "aliens", "mind control", "microchip", "microchips",
    "insider reveals", "whistleblower", "big pharma", "secret society",
    "proves the moon landing", "time travel", "live to 150", "live forever",
    "reverse aging", "lose 10 kilos", "5g towers", "anonymous source claims",
]


def clean_text(text: str) -> str:
    """Lowercase, strip URLs/extra whitespace. Kept deliberately simple -
    TfidfVectorizer handles tokenization and stopwords itself."""
    text = text.lower()
    text = re.sub(r"http\S+|www\.\S+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def find_red_flags(text: str):
    """Return the list of red-flag phrases found in the text (case-insensitive)."""
    lowered = text.lower()
    return [phrase for phrase in RED_FLAG_PHRASES if phrase in lowered]
