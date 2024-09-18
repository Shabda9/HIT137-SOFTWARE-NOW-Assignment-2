import pandas as pd

def extract_and_save_text(csv_files, output_file):
    """
    Extracts text from specified columns in multiple CSV files and saves them to a single text file.

    Parameters:
        csv_files (list of tuples): Each tuple contains the name of a CSV file and the name of the column with the text data.
        output_file (str): The name of the text file where the extracted text will be saved.
    """
    # List to store all extracted text from the CSV files
    all_texts = []

    # Process each CSV file to extract text data
    for (file, text_column) in csv_files:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file)

        # Check if the specified text column exists in the DataFrame
        if text_column in df.columns:
            # Convert text data to string and add to the list
            all_texts.extend(df[text_column].astype(str).tolist())

    # Write all collected text data to the output text file
    with open(output_file, 'w', encoding='utf-8') as f:
        for text in all_texts:
            f.write(text + '\n')

    print(f'Text information written to {output_file}')

# Example usage
csv_files = [('CSV1.csv', 'SHORT-TEXT'), ('CSV2.csv', 'TEXT'), ('CSV3.csv', 'TEXT'), ('CSV4.csv', 'TEXT')]
output_file = 'all_csv_file.txt'
extract_and_save_text(csv_files, output_file)
