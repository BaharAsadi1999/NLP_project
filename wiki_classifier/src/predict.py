import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from cleaningprocess import TextPreprocessor


with open(r'C:\Users\Asus\PycharmProjects\NLP_project\wiki_classifier\src\model.pkl', 'rb') as f:
    model = pickle.load(f)


vectorizer = TfidfVectorizer()
vectorizer.fit(pd.read_csv(r'C:\Users\Asus\PycharmProjects\NLP_project\wiki_classifier\data\tfidf_matrix.csv').columns)


preprocessor = TextPreprocessor()


def predict(text):
    processed = preprocessor.full_preprocess(text)
    vectorized = vectorizer.transform([processed])
    prediction = model.predict(vectorized)
    return 'Geographic' if prediction[0] == 1 else 'Non-Geographic'


if __name__ == "__main__":
    sample_text = "I love studying"
    print("Prediction:", predict(sample_text))






