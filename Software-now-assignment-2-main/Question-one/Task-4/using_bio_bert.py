from transformers import BertTokenizer, BertForTokenClassification
import torch

# Load the BioBERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('monologg/biobert_v1.1_pubmed', do_lower_case=False)
model = BertForTokenClassification.from_pretrained('monologg/biobert_v1.1_pubmed', num_labels=2)  # Assuming 2 labels for 'DISEASE' and 'DRUG'
print(tokenizer.convert_ids_to_tokens(range(model.config.num_labels)))

# Function to identify entities within a text
def identify_entities_in_text(text):
    """
    Identifies entities in the input text using the BioBERT model.

    Parameters:
        text (str): The input text to process for entity extraction.

    Returns:
        list of tuples: A list containing tuples of tokens and their corresponding entity labels.
    """
    # Tokenize the input text and generate model predictions
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=2)

    # Map the predicted labels to the corresponding tokens
    entities = []
    for token, prediction in zip(inputs["input_ids"][0], predictions[0]):
        token_str = tokenizer.convert_ids_to_tokens(token.item())
        label = 'DISEASE' if torch.eq(prediction, torch.tensor(1)) else 'DRUG' if torch.eq(prediction, torch.tensor(0)) else 'O'
        
        if label != 'O':
            entities.append((token_str, label))

    return entities

# Read and process the text file
file_path = '/Users/girishiva/Desktop/class/Semester-2/Software Now/Assingment-2/all_csv_file.txt' # Replace with the actual path to your text file

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
    entities = identify_entities_in_text(text)

# Separate 'DISEASE' and 'DRUG' entities
diseases = [entity[0] for entity in entities if entity[1] == 'DISEASE']
drugs = [entity[0] for entity in entities if entity[1] == 'DRUG']

# Output the results
print("Diseases:", diseases)
print("Drugs:", drugs)
