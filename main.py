import spacy
from collections import Counter
import re

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Open and read the contents of the complaints.txt file
with open('complaints.txt', 'r') as file:
    text = file.read()


# Function to preprocess the text
def preprocess_text(text):
    # Remove numbers and punctuation, convert to lowercase
    text = re.sub(r'[0-9]+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    return text


# Preprocess the text
preprocessed_text = preprocess_text(text)

# Process the text with SpaCy
doc = nlp(preprocessed_text)

# Define the part-of-speech classes to keep
pos_classes_to_keep = {"NOUN", "VERB", "ADJ", "ADV", "PROPN"}


# Function to filter words based on their part-of-speech class
def filter_words_by_pos(doc, pos_classes_to_keep):
    filtered_words = [token.text for token in doc if token.pos_ in pos_classes_to_keep]
    return " ".join(filtered_words)


# Filter out words with specified part-of-speech classes
filtered_text = filter_words_by_pos(doc, pos_classes_to_keep)

# Tokenize the filtered text into words
words = filtered_text.split()


# Function to find the most common words and phrases
def find_most_common_words_and_phrases(words, n):
    # Create a Counter object to count word occurrences
    word_counter = Counter(words)

    # Find the most common words
    most_common_words = word_counter.most_common(n)

    return most_common_words


# Set the number of most common words and phrases you want to find
num_most_common = 10

# Find and print the most common words and phrases
most_common_words = find_most_common_words_and_phrases(words, num_most_common)

# Print the results
print("Most Common Words and Phrases:")
for i, (word, count) in enumerate(most_common_words, 1):
    print(f"{i}. {word}: {count} times")

# Extract the most common words as a list
common_words = [word for word, count in most_common_words]

# Join the common words to create a conclusive sentence
conclusive_sentence = " ".join(common_words)

# Print the conclusive sentence
print(f"Conclusive Sentence: {conclusive_sentence}")
"""Conclusive sentence will not be syntactic and may come as meaningless to you!"""