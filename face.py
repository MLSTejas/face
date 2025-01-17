# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VLzlUK_hQbwEECT3BhJAE2rBWrnesCd2
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import re
import streamlit as st

# Load the dataset
data = pd.read_csv("emotion dataset.csv")
text = data["Words"]
labels = data["Emotion"]

# Text preprocessing (consider additional steps like stemming/lemmatization)
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove punctuation and special characters
    return text

# Feature extraction using TF-IDF
vectorizer = TfidfVectorizer()
features = vectorizer.fit_transform(text.apply(preprocess_text))

#Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Model training: Logistic Regression (replace with other models as needed)
model = LogisticRegression(multi_class="multinomial", solver="lbfgs")
model.fit(X_train, y_train)

# Function to classify new text paragraphs
def classify_text(new_text):
    new_features = vectorizer.transform([preprocess_text(new_text)])
    predicted_label = model.predict(new_features)[0]
    return predicted_label

# Streamlit for real-time input
st.title("Real-Time Text Emotion Classification")
new_text_input = st.text_input("Enter your text paragraph:")

if st.button("Classify"):
    if new_text_input:
        predicted_emotion = classify_text(new_text_input)
        st.success(f"Predicted emotion: {predicted_emotion}")
    else:
        st.warning("Please enter some text to classify.")

