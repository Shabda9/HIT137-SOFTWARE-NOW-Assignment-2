
import csv
from collections import Counter
import re

def extract_top_words(file_path, output_csv_path, top_n=30):
    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Preprocess the text (remove non-alphanumeric characters and convert to lowercase)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.lower().split()

    # Count word occurrences using counter class
    word_counts = Counter(words)

    # Get the top 30 words
    top_words = word_counts.most_common(top_n)

    # Save the top words to a CSV file
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Word', 'Count'])  # Header row

        for word, count in top_words:
            csv_writer.writerow([word, count])

# Example usage
file_path = 'all_csv_file.txt'
output_csv_path = 'top_words.csv'
extract_top_words(file_path, output_csv_path)