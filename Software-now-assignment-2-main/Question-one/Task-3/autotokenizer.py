from transformers import AutoTokenizer
from collections import Counter
from concurrent.futures import ProcessPoolExecutor

def tokenize_and_count(chunk, model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(chunk)))
    return Counter(tokens)

def read_chunks(file_path, chunk_size=10 * 1024 * 1024):
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

def count_and_display_top_tokens(file_path, model_name, top_n=30, num_processes=2):
    # Tokenize and count in parallel
    if __name__ == '__main__':
        with ProcessPoolExecutor(max_workers=num_processes) as executor:
            token_counters = list(executor.map(tokenize_and_count, read_chunks(file_path), [model_name] * num_processes))

        # Combine the results
        combined_counter = sum(token_counters, Counter())

        # Display the top N tokens
        top_tokens = combined_counter.most_common(top_n)
        print(f"Top {top_n} tokens:")
        for token, count in top_tokens:
            print(f"{token}: {count}")

# Example usage:
file_path = '/Users/nandukhanal/Documents/Classworks/Semester-1/Software Now/Assingment-2/Question-one/all_csv_file.txt'
model_name = 'bert-base-uncased'  # You can use any model name from the transformers library
count_and_display_top_tokens(file_path, model_name)
