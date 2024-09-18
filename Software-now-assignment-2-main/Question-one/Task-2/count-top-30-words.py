import csv
from collections import Counter
import re

def save_most_frequent_words(input_text_file, output_csv_file, number_of_words=30):
    """
    Extracts the most frequent words from a text file and saves them to a CSV file.

    Parameters:
        input_text_file (str): Path to the input text file.
        output_csv_file (str): Path to the output CSV file where the words and their counts will be saved.
        number_of_words (int): The number of top frequent words to extract. Default is 30.
    """
    # Read the content of the input text file
    with open(input_text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Preprocess the text (remove non-alphanumeric characters and convert to lowercase)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.lower().split()

    # Count the occurrences of each word using Counter
    word_counts = Counter(words)

    # Get the most frequent words
    top_words = word_counts.most_common(number_of_words)

    # Write the top words and their counts to a CSV file
    with open(output_csv_file, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Word', 'Count'])  # Write header row

        for word, count in top_words:
            csv_writer.writerow([word, count])

# Example usage
input_text_file = 'all_csv_file.txt'
output_csv_file = 'top_words.csv'
save_most_frequent_words(input_text_file, output_csv_file)
