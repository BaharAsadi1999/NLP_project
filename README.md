📌 Assignment 1: Wikipedia Text Classification
Objective:
Automatically classify Wikipedia articles as either Geographic (e.g., countries, cities) or Non-Geographic (e.g., people, events).

Key Components:

Data Collection: 
Articles were gathered using the Wikipedia API.
Preprocessing: Tokenization, stopword removal, lemmatization using NLTK and SpaCy.
Feature Extraction: TF-IDF vectorization.
Model: Logistic Regression with class balancing.
Evaluation: High accuracy with a confusion matrix showing strong performance (e.g., 49 true positives, 0 false positives).
Deployment: Modular Python scripts with a clear project structure and documentation.


📌 Assignment 2: Text Style-Adaptive Summarization

Objective:
Generate a summary of a content document that mimics the style of a separate reference document.

Key Features:

Style Analysis: Extracts stylistic features like sentence length and vocabulary richness.

Hierarchical Summarization: Handles long texts by summarizing in chunks and recursively condensing.

Output: Produces a styled summary and a query prompt for further use.

Tools Used:

Python, NLTK, custom summarization logic.

🧰 Technologies & Tools
Languages & Libraries: 
Python 3.10+, NLTK, SpaCy, scikit-learn

Data Sources: Wikipedia API

Project Structure: Modular with clear separation of data, preprocessing, modeling, and inference.
