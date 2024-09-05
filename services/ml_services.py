from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

def classify_data():
    # Example dataset for classification
    data = [
        {"text": "Flood in Mumbai", "category": "flood"},
        {"text": "Earthquake in Delhi", "category": "earthquake"}
    ]
    
    # Convert data into a Pandas DataFrame
    df = pd.DataFrame(data)
    
    # Prepare feature extraction
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['text'])
    
    # Train simple Naive Bayes classifier
    model = MultinomialNB()
    model.fit(X, df['category'])
    
    # Classify new data (example)
    test_data = ["Tsunami warning in Japan"]
    test_vector = vectorizer.transform(test_data)
    prediction = model.predict(test_vector)
    
    return {"text": test_data[0], "category": prediction[0]}
