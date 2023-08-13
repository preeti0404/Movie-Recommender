import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
import re
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

personalities = {0: 'ENFJ',
                 1: 'ENFP',
                 2: 'ENTJ',
                 3: 'ENTP',
                 4: 'ESFJ',
                 5: 'ESFP',
                 6: 'ESTJ',
                 7: 'ESTP',
                 8: 'INFJ',
                 9: 'INFP',
                 10: 'INTJ',
                 11: 'INTP',
                 12: 'ISFJ',
                 13: 'ISFP',
                 14: 'ISTJ',
                 15: 'ISTP'}


def transform_text(text):
    text = text.lower()
    text = re.sub('https?://[^\s<>"]+|www\.[^\s<>"]+', ' ', text)
    text = nltk.word_tokenize(text)
    ls = []
    for word in text:
        if word .isalnum():
            ls.append(word)
    text = ls[:]
    ls.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            ls.append(i)
    text = ls[:]
    ls.clear()

    for i in text:
        ls.append(ps.stem(i))

    return " ".join(ls)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("MBTI Personality Classifier")

input_sms = st.text_area("Enter your most recent social media text post")

if st.button('Predict'):
    transformed_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input.toarray())
    st.header(f'Your Personality:- {personalities[result[0]]}')
    
else:
    st.header(f'Calculating ...')
