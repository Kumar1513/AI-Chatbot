import random
import json
import nltk
import os
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

current_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(current_dir, r"C:\Users\Kumar Ganesh\mlproject2\intent.json")) as file:
    data = json.load(file)

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def predict_class(sentence):
    sentence_words = clean_up_sentence(sentence)
    for intent in data['intents']:
        if any(word in intent['patterns'] for word in sentence_words):
            return intent['tag']
    return "noanswer"

def get_response(tag):
    for intent in data['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

def chatbot_response(msg):
    tag = predict_class(msg)
    response = get_response(tag)
    return response
