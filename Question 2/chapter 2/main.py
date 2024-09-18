# Import necessary functions from other modules
from string_operations import separate_string
from decryption import decrypt, find_shift_key
from ascii_conversions import convert_even_numbers, convert_uppercase_letters


def main():
    # Example input string
    s = "56aAww1984sktr235270aYmn145ss785fsq31D0"

    print("Given String:", s)
    # Separate the string into numbers and letters
    num_string, letter_string = separate_string(s)

    print("Number string:", num_string)
    print("Letter string:", letter_string)

    # Convert even numbers to ASCII values
    even_num_ascii = convert_even_numbers(num_string)
    print("ASCII values of even numbers:", even_num_ascii)

    # Convert uppercase letters to ASCII values
    uppercase_ascii = convert_uppercase_letters(letter_string)
    print("ASCII values of uppercase letters:", uppercase_ascii)

    # Cryptogram to decrypt
    cryptogram = """
    VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY
    NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
    URYYQBAG QRFREIR ZR NG ZL ORFG ZNEWLA ZBAEBR
    """

    # Find the correct shift key
    shift_key = find_shift_key(cryptogram)
    # Decrypt the cryptogram using the found shift key
    decrypted_text = decrypt(cryptogram, shift_key)

    print(f"\nFound shift key: {shift_key}")
    print("Decrypted text:")
    print(decrypted_text)


# Ensure the main function only runs if this script is executed directly
if __name__ == "__main__":
    main()
