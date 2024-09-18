def extract_and_transform(input_string):
    """
    Separates digits and letters from the input string, processes even numbers and uppercase letters, 
    and converts them to their ASCII values.

    Parameters:
        input_string (str): The input string containing both letters and numbers.

    Returns:
        tuple: A tuple containing the extracted numbers string, letters string, list of even numbers, 
               ASCII values of even numbers, list of uppercase letters, and ASCII values of uppercase letters.
    """
    # Extract numbers and letters separately
    numbers_only = ''.join(char for char in input_string if char.isdigit())
    letters_only = ''.join(char for char in input_string if char.isalpha())

    # Process even numbers and get their ASCII values
    even_numbers = [int(digit) for digit in numbers_only if int(digit) % 2 == 0]
    ascii_values_of_evens = [ord(str(num)) for num in even_numbers]

    # Extract uppercase letters and get their ASCII values
    uppercase_letters = [char for char in letters_only if char.isupper()]
    ascii_values_of_uppercase = [ord(char) for char in uppercase_letters]

    return numbers_only, letters_only, even_numbers, ascii_values_of_evens, uppercase_letters, ascii_values_of_uppercase

def main_extraction():
    """
    Demonstrates the extraction and transformation process on a sample input string.
    """
    input_string = 'ajsdb1fy584g9bf199u24dfb60AgjhGQfdhgzGF8dfKH77Zredz9vF'

    # Extract and transform the input string
    numbers_only, letters_only, even_numbers, ascii_values_of_evens, uppercase_letters, ascii_values_of_uppercase = extract_and_transform(input_string)

    # Display the results
    print(f"Numbers String: {numbers_only}")
    print(f"Letters String: {letters_only}")
    print(f"Even Numbers: {even_numbers}")
    print(f"Even Numbers ASCII Values: {ascii_values_of_evens}")
    print(f"Uppercase Letters: {uppercase_letters}")
    print(f"Uppercase Letters ASCII Values: {ascii_values_of_uppercase}")

if __name__ == "__main__":
    main_extraction()

# Decryption functions
def caesar_cipher_decrypt(ciphertext, shift):
    """
    Decrypts a given text encrypted using the Caesar cipher with a specified shift.

    Parameters:
        ciphertext (str): The encrypted text.
        shift (int): The number of positions each character in the text is shifted.

    Returns:
        str: The decrypted text.
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Decrypt only alphabetical characters
            if char.islower():
                plaintext += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                plaintext += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            # Keep non-alphabetical characters unchanged
            plaintext += char
    return plaintext

def determine_caesar_shift_key(ciphertext):
    """
    Determines the most likely shift key for a Caesar cipher by checking for common English words.

    Parameters:
        ciphertext (str): The encrypted text.

    Returns:
        int or None: The shift key if found, otherwise None.
    """
    for shift in range(1, 26):
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        # Check if the decrypted text contains common English words
        if any(word in decrypted_text.lower() for word in ['the', 'and', 'you', 'for']):
            return shift
    return None

def main_decryption():
    """
    Attempts to decrypt a Caesar cipher encrypted message by determining the shift key and then decrypting.
    """
    cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
    shift_key = determine_caesar_shift_key(cryptogram)

    if shift_key is not None:
        decrypted_message = caesar_cipher_decrypt(cryptogram, shift_key)
        print(f"The shift key is: {shift_key}")
        print(f"The decrypted message is: {decrypted_message}")
    else:
        print("Unable to determine the shift key.")

if __name__ == "__main__":
    main_decryption()
