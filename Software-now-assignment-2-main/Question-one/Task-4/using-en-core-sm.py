import spacy
from concurrent.futures import ThreadPoolExecutor

# Load the spaCy model
nlp = spacy.load("en_core_sci_sm")
nlp.disable_pipes('parser', 'ner')

# Function to process a batch of text within a chunk
def process_batch(chunk):
    docs = nlp.pipe(chunk, disable=["parser", "ner"])
    
    # Extract disease and drug entities
    diseases = []
    drugs = []

    for doc in docs:
        diseases.extend([ent.text for ent in doc.ents if ent.label_ == "DISEASE"])
        drugs.extend([ent.text for ent in doc.ents if ent.label_ == "CHEMICAL"])

    return diseases, drugs

# Function to process a large text file in batches
def process_large_text_file(file_path, chunk_size=10 * 1024 * 1024, batch_size=10):
    with open(file_path, "r", encoding="utf-8") as file:
        # Read the file in chunks to avoid loading the entire file into memory
        chunks = []
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break  # End of file
            chunks.append(chunk)
            if len(chunks) == batch_size:
                yield chunks
                chunks = []

        # Yield the remaining chunks
        if chunks:
            yield chunks

# Process each batch of chunks concurrently
def process_batches(batches):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_batch, batches))

    # Aggregate results
    all_diseases = [disease for result in results for disease in result[0]]
    all_drugs = [drug for result in results for drug in result[1]]

    # Print the extracted diseases and drugs
    print("Diseases:", all_diseases)
    print("Drugs:", all_drugs)

    return all_diseases, all_drugs

# Example usage:
file_path = '/Users/nandukhanal/Documents/Classworks/Semester-1/Software Now/Assingment-2/Question-one/all_csv_file.txt'
chunk_size = 100000  # Adjust as needed
batch_size = 10
batches = process_large_text_file(file_path, chunk_size=chunk_size, batch_size=batch_size)

# Process batches
process_batches(batches)
