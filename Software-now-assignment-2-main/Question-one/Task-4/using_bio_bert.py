from transformers import BertTokenizer, BertForTokenClassification
import torch

# Load BioBERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('monologg/biobert_v1.1_pubmed', do_lower_case=False)
model = BertForTokenClassification.from_pretrained('monologg/biobert_v1.1_pubmed', num_labels=2)  # Assuming 2 labels for 'DISEASE' and 'DRUG'
print(tokenizer.convert_ids_to_tokens(range(model.config.num_labels)))
# Function to extract entities from a text
def extract_entities(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=2)

    # Map token predictions to entities
    entities = []
    for token, prediction in zip(inputs["input_ids"][0], predictions[0]):
        token_str = tokenizer.convert_ids_to_tokens(token.item())
        label = 'DISEASE' if torch.eq(prediction, torch.tensor(1)) else 'DRUG' if torch.eq(prediction, torch.tensor(0)) else 'O'
        
        if label != 'O':
            entities.append((token_str, label))

    return entities

# Process the text file
file_path = '/Users/nandukhanal/Documents/Classworks/Semester-1/Software Now/Assingment-2/Question-one/all_csv_file.txt'  # Replace with the actual path to your text file

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
    entities = extract_entities(text)

# Separate 'diseases' and 'drugs'
diseases = [entity[0] for entity in entities if entity[1] == 'DISEASE']
drugs = [entity[0] for entity in entities if entity[1] == 'DRUG']

# Print the results
print("Diseases:", diseases)
print("Drugs:", drugs)
