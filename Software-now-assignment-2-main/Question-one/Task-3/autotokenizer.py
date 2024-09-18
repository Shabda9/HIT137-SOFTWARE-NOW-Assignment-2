from transformers import AutoTokenizer
from collections import Counter
from concurrent.futures import ProcessPoolExecutor

def tokenize_and_count_tokens(chunk, tokenizer_model_name):
    """
    Tokenizes a chunk of text and counts the occurrences of each token using a specified tokenizer model.

    Parameters:
        chunk (str): A chunk of text to be tokenized.
        tokenizer_model_name (str): The name of the tokenizer model from the transformers library.

    Returns:
        Counter: A Counter object with token counts.
    """
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_model_name)
    tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(chunk)))
    return Counter(tokens)

def read_file_in_chunks(file_path, chunk_size=10 * 1024 * 1024):
    """
    Reads a file in chunks of specified size.

    Parameters:
        file_path (str): The path to the file to be read.
        chunk_size (int): The size of each chunk in bytes. Default is 10MB.

    Yields:
        str: A chunk of text from the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

def process_and_show_top_tokens(input_file_path, tokenizer_model_name, top_n_tokens=30, max_processes=2):
    """
    Tokenizes the text in a file, counts the tokens using multiple processes, and displays the top N tokens.

    Parameters:
        input_file_path (str): The path to the input text file.
        tokenizer_model_name (str): The name of the tokenizer model from the transformers library.
        top_n_tokens (int): The number of top tokens to display. Default is 30.
        max_processes (int): The number of processes to use for parallel processing. Default is 2.
    """
    # Tokenize and count in parallel
    if __name__ == '__main__':
        with ProcessPoolExecutor(max_workers=max_processes) as executor:
            token_counters = list(executor.map(tokenize_and_count_tokens, read_file_in_chunks(input_file_path), [tokenizer_model_name] * max_processes))

        # Combine the results from all processes
        combined_counter = sum(token_counters, Counter())

        # Display the top N tokens
        top_tokens = combined_counter.most_common(top_n_tokens)
        print(f"Top {top_n_tokens} tokens:")
        for token, count in top_tokens:
            print(f"{token}: {count}")

# Example usage:
input_file_path = '/Users/girishiva/Desktop/class/Semester-2/Software Now/Assingment-2/all_csv_file.txt'
tokenizer_model_name = 'bert-base-uncased'  # You can use any model name from the transformers library
process_and_show_top_tokens(input_file_path, tokenizer_model_name)
