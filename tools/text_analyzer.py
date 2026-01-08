"""
Text Analyzer Tool
Provides word count, character count, and basic sentiment.
"""

from langchain.tools import tool


@tool
def analyze_text(text: str) -> dict:
    """
summary:
    This function computes the number of words, number of characters,
    and performs a simple rule-based sentiment analysis based on the
    presence of predefined positive and negative words.

Args:
    text (str): The input text to be analyzed.

Returns:
    dict: A dictionary containing:
        - word_count (int): Total number of words in the text.
        - sentiment (str): Sentiment classification of the text.
"""
    try:
        words = text.split()
        char_count = len(text)

        positive_words = ["good", "great", "excellent", "happy", "love"]
        negative_words = ["bad", "poor", "sad", "hate", "terrible"]

        sentiment_score = 0
        for word in words:
            if word.lower() in positive_words:
                sentiment_score += 1
            elif word.lower() in negative_words:
                sentiment_score -= 1

        sentiment = "Neutral"
        if sentiment_score > 0:
            sentiment = "Positive"
        elif sentiment_score < 0:
            sentiment = "Negative"

        return {
            "word_count": len(words),
            "character_count": char_count,
            "sentiment": sentiment
        }

    except Exception as e:
        return {"error": str(e)}