
# Common Words Analyzer
## Description

This Python project analyzes a text document to find the most common words and phrases. It also uses natural language processing (NLP) to preprocess the text and filter out specific part-of-speech classes.
## Overview

The Common Words Analyzer is a Python program designed to analyze a given text and identify the most frequent words and phrases within it. It utilizes the SpaCy library for natural language processing to extract relevant words and phrases based on their part-of-speech classes (e.g., nouns, verbs, adjectives, adverbs, and proper nouns).

## Usefulness of the Program

This program serves multiple purposes and can be useful in various scenarios:

1. **Content Analysis**: Content creators, writers, and researchers can use this program to gain insights into the most common words and phrases in a text. This information can help in improving writing style, identifying key themes, and ensuring clarity in communication.

2. **Text Summarization**: By extracting the most common words and phrases, the program can help in generating concise summaries of lengthy texts. This is particularly useful for condensing information and making it more digestible.

3. **Keyword Extraction**: SEO professionals and marketers can utilize the program to identify relevant keywords and phrases within a body of text. This aids in optimizing content for search engines and improving online visibility.

4. **Research and Analysis**: Researchers can use this program to analyze textual data, identifying trends and patterns in language usage. This can be applied in fields such as linguistics, sociology, and psychology.

5. **Content Enhancement**: Writers can use the program to identify repetitive words and phrases in their work, allowing them to diversify their vocabulary and enhance the overall quality of their writing.

## Conclusive Sentence

The program also generates a "conclusive sentence" based on the most common words and phrases it identifies. This sentence is formed by joining these common words and phrases together.

**WARNING**: The conclusive sentence may not always be syntactic or meaningful. It is a concatenation of the most frequent terms and is generated for the sake of providing a brief summary of the text's content. Users should exercise caution and not rely solely on this sentence for extracting the full context of the text.

## Limitations

- The program relies on the accuracy of the SpaCy language model for part-of-speech tagging. Inaccuracies in tagging may lead to incorrect results.

- Stop words and certain word classes (e.g., prepositions, pronouns) are excluded from the analysis. However, the exclusion list can be customized as per project requirements.

- The conclusive sentence is a simple concatenation of common words and may not reflect the nuanced meaning of the text.

- This program is designed for English text and may not perform optimally with texts in other languages.

## Getting Started

To use the Common Words Analyzer, follow these steps:

1. Ensure you have Python installed on your system.

2. Install the required Python libraries using `pip`:


### Prerequisites

- Python 3.x
- spaCy library (for NLP processing)

### Installation

1. Clone this repository:

2. Install the required libraries:

### Usage

1. Place your text document (e.g., `complaints.txt`) in the project directory.

2. Run the script to analyze the common words and phrases:
3. The script will output the most common words and phrases found in the document.

4. You can adjust the number of common words to display and customize word filtering options by editing the `main.py` file.

### Configuration

- You can configure the number of most common words to display by changing the `num_most_common` variable in `main.py`.
- You can customize word filtering based on part-of-speech classes by modifying the `pos_classes_to_keep` set in `main.py`.

### Example

- An example input text (`complaints.txt`) is provided for demonstration purposes.
- The script will exclude common words like "the," "and," and "in" and focus on nouns, verbs, adjectives, adverbs, and proper nouns to find the most relevant words and phrases.
