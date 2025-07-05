# Assignment 1  

## Overview  
This project implements a text classification system that categorizes English texts into geographic and nongero. 
The solution uses Wikipedia data along with  **Logistic Regression**.

## Features  
- **Text Classification**: Predicts whether a given text is geographic or non-geographic.  
- **Preprocessing Options**:  
  - **Stopword Removal** 
  - **Stemming** 
  - **Lemmatization**  
- **Feature Extraction**:  
  - **TF-IDF**
- **Model Choices**:
  - **Logistic Regression**   

## Requirements  
### Python Version (NLTK/Spacy):  
- Python 3.11+  
- Libraries:  
  - `nltk` (for preprocessing & Naive Bayes)  
  - `spacy` (for advanced NLP pipelines)  
  - `scikit-learn` (for Logistic Regression)  
  - `wikipedia-api` (for fetching Wikipedia data)  
   ```python
   pip install -r requirements.txt
   ```
## Project Structure
wiki_classifier/
├── data/                          # Raw and processed datasets
│   ├── wiki_dataset.csv           # Raw Wikipedia dataset
│   ├── processed_dataset.csv      # Cleaned/preprocessed data
│   └── tfidf_matrix.csv         # Feature matrices  
│   
│
├── src/                           # Source code
    └── dataloader.py # Wikipedia data fetcher 
│   ├── cleaningprocess.py          # Data preprocessing scripts
│   ├── extractfeatures.py          # Feature visualization
│   ├── model.py                   # Model training (Naive Bayes/Logistic Regression)
│   ├── predict.py                 # Prediction script
│   ├── utils.py                   # Helper functions
│   └── model.pkl                  # Trained model (serialized)
│   └── confusion_matrix.png       # Performance metrics
│  
│
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation

## Implementation Pipeline  
1. **Data Collection**:  
   - Fetch annotated Wikipedia articles using the MediaWiki API.  
2. **Preprocessing**:  
   - Tokenization, stopword removal, stemming/lemmatization.  
3. **Feature Extraction**:  
   - TF-IDF  
4. **Model Training**:  
   -  Logistic Regression.  
5. **Classification**:  
   - Predict class (geographic/non-geographic) for input text.  


