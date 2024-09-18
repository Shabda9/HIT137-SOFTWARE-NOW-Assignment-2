import pandas as pd

# List of CSV file names and thier text columns
csv_files = [('CSV1.csv', 'SHORT-TEXT'), ('CSV2.csv', 'TEXT'), ('CSV3.csv','TEXT'), ('CSV4.csv','TEXT')]

# List to store text information from all files
all_texts = []

# Read each CSV file and extract text information
for (file, text_column) in csv_files:
    # Read CSV file into a DataFrame
    df = pd.read_csv(file)

    # Assuming 'text' is the column containing text information
    if text_column in df.columns:
        # Extract text information and append to the list
        all_texts.extend(df[text_column].astype(str).tolist())

# Write text information to a new text file
output_file = 'all_csv_file.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    for text in all_texts:
        f.write(text + '\n')

print(f'Text information written to {output_file}')