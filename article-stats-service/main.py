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

# Configure logging level to see INFO messages 
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
        "avg_sentence_length": round(len(clean_words) / len(sentences), 2) if sentences else 0,
        "top_5_words": [word for word, count in Counter(clean_words).most_common(5)]
    }

    return stats

@app.route('/analyze', methods=['POST'])
def analyze_article():
    """
    This endpoint accepts article text and returns statistics.
    """
    try:
        # Handle different input 
        if request.is_json:
            data = request.get_json()
            text = data.get('text', '')
        else:
            text = request.form.get('text', '')

        # Validate input exists
        if not text.strip():
            return jsonify({"error": "No text provided"}), 400
            # 400 = Bad Request (client sent invalid data)

        # Log successful processing 
        app.logger.info(f"Processing article with {len(text)} characters")

        # Process the text
        stats = calculate_article_stats(text)
        return jsonify(stats)

    except Exception as e:
        # Log errors
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500
        # 500 = Server Error (something went wrong internally)

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify service is running.
    """
    return jsonify({"status": "healthy", "service": "article-stats"})

@app.route('/', methods=['GET'])
def index():
    """
    Root endpoint to provide basic information about available endpoints.
    """
    return jsonify({
        "message": "Article Statistics Microservice",
        "endpoints": {
            "/analyze": "POST - Submit article text for analysis",
            "/health": "GET - Check service health status",
            "/": "GET - This documentation"
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # Start development server
    # host='0.0.0.0' to make it accessible from other devices
    # debug=True to enable auto-reload when code is edited
