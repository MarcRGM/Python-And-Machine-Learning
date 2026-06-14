from flask import Flask, request, jsonify
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
import logging

# Download required NLTK data files
# punkt contains pre-trained models for sentence/word splitting
nltk.download('punkt', quiet=True)

# Initialize web application
app = Flask(__name__)

# Configure logging level - see INFO messages and above
app.logger.setLevel(logging.INFO)

def calculate_article_stats(text):
    """
    It takes raw article text and returns calculated statistics.
    """
    # Break text into sentences (handles . from words)
    sentences = sent_tokenize(text)

    # Break text into words and lowercase them
    words = word_tokenize(text.lower())

    # Remove punctuation and numbers (keep only letters)
    clean_words = [word for word in words if word.isalnum()]

    # Calculate statistics
    stats = {
        "word_count": len(clean_words),
        "sentence_count": len(sentences),
        "avg_sentence_length": round(len(clean_words) / len(sentences), 2) if sentences else 0
    }

    return stats

