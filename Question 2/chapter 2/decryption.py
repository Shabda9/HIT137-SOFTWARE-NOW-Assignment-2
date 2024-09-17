def decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Determine the ASCII offset based on letter case
            ascii_offset = 65 if char.isupper() else 97
            # Decrypt the character using the Caesar cipher formula
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            # Keep non-alphabetic characters unchanged
            plaintext += char
    return plaintext

def score_text(text):
    # List of common English words to check for
    common_words = set(['THE', 'BE', 'TO', 'OF', 'AND', 'IN', 'THAT', 'HAVE', 'IT', 'FOR', 'YOU', 'WITH', 'ON', 'AT'])
    # Split the text into words and convert to uppercase
    words = text.upper().split()
    # Count how many common words appear in the text
    return sum(word in common_words for word in words)

def find_shift_key(ciphertext):
    best_score = 0
    best_shift = 0
    # Try all possible shift values (0-25)
    for shift in range(26):
        # Decrypt the text with the current shift
        plaintext = decrypt(ciphertext, shift)
        # Score the decrypted text
        score = score_text(plaintext)
        # Update best score and shift if current score is higher
        if score > best_score:
            best_score = score
            best_shift = shift
    return best_shift