import spacy
from concurrent.futures import ThreadPoolExecutor

# Load the spaCy model and disable unnecessary components to speed up processing
nlp = spacy.load("en_core_sci_sm")
nlp.disable_pipes('parser', 'ner')

# Function to process a list of text documents and extract entities
def extract_entities_from_batch(text_batch):
    """
    Processes a batch of text and extracts disease and drug entities using spaCy.

    Parameters:
        text_batch (list of str): A batch of text documents.

    Returns:
        tuple: A tuple containing two lists - one for diseases and another for drugs.
    """
    docs = nlp.pipe(text_batch, disable=["parser", "ner"])
    
    # Initialize lists to store entities
    diseases = []
    drugs = []

    for doc in docs:
        diseases.extend([ent.text for ent in doc.ents if ent.label_ == "DISEASE"])
        drugs.extend([ent.text for ent in doc.ents if ent.label_ == "CHEMICAL"])

    return diseases, drugs

# Function to read a large text file in chunks and yield them as batches
def read_large_file_in_batches(file_path, chunk_size=10 * 1024 * 1024, batch_size=10):
    """
    Reads a large text file in chunks and groups them into batches.

    Parameters:
        file_path (str): The path to the text file to be processed.
        chunk_size (int): The size of each chunk to read from the file in bytes.
        batch_size (int): The number of chunks to include in each batch.

    Yields:
        list of str: A batch containing a list of text chunks.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        chunks = []
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break  # Reached end of file
            chunks.append(chunk)
            if len(chunks) == batch_size:
                yield chunks
                chunks = []

        # Yield any remaining chunks
        if chunks:
            yield chunks

# Function to process batches of text concurrently and extract entities
def extract_entities_from_batches_concurrently(batches):
    """
    Processes batches of text concurrently to extract disease and drug entities.

    Parameters:
        batches (generator): A generator that yields batches of text.

    Returns:
        tuple: A tuple containing two lists - all extracted diseases and all extracted drugs.
    """
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(extract_entities_from_batch, batches))

    # Aggregate the results from all batches
    all_diseases = [disease for result in results for disease in result[0]]
    all_drugs = [drug for result in results for drug in result[1]]

    # Output the extracted entities
    print("Diseases:", all_diseases)
    print("Drugs:", all_drugs)

    return all_diseases, all_drugs

# Example usage:
file_path = '/Users/girishiva/Desktop/class/Semester-2/Software Now/Assingment-2/all_csv_file.txt'
chunk_size = 100000  # Adjust as needed
batch_size = 10
batches = read_large_file_in_batches(file_path, chunk_size=chunk_size, batch_size=batch_size)

# Process the batches and extract entities
extract_entities_from_batches_concurrently(batches)
