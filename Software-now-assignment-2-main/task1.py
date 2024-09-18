def separation_and_conversion(a):
    number_string = ''.join(b for b in a if b.isdigit())
    letter_string = ''.join(b for b in a if b.isalpha())

    even_numbers = [int(number) for number in number_string if int(number) % 2 == 0]
    ascii_value_numbers = [ord(str(number)) for number in even_numbers]

    uppercase_letters = [character for character in letter_string if character.isupper()]
    ascii_value_letters = [ord(character) for character in uppercase_letters]

    return number_string, letter_string, even_numbers, ascii_value_numbers, uppercase_letters, ascii_value_letters

def main():
    input_string = 'ajsdb1fy584g9bf199u24dfb60AgjhGQfdhgzGF8dfKH77Zredz9vF'

    number_string, letter_string, even_numbers, ascii_value_numbers, uppercase_letters, ascii_value_letters = separation_and_conversion(input_string)

    print(f"Numbers String: {number_string}")
    print(f"Letters String: {letter_string}")
    print(f"Even Numbers: {even_numbers}")
    print(f"Even Numbers ASCII Values: {ascii_value_numbers}")
    print(f"Uppercase Letters: {uppercase_letters}")
    print(f"Uppercase Letters ASCII Values: {ascii_value_letters}")

if __name__ == "__main__":
    main()

#decrytion
def decrypt(ciphertext, shift):
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

def find_shift_key(ciphertext):
    for shift in range(1, 26):
        decrypted_text = decrypt(ciphertext, shift)
        # Check if the decrypted text contains common English words
        if any(word in decrypted_text.lower() for word in ['the', 'and', 'you', 'for']):
            return shift
    return None

def main():
    cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR" 
    shift_key = find_shift_key(cryptogram)

    if shift_key is not None:
        decrypted_quote = decrypt(cryptogram, shift_key)
        print(f"The shift key is: {shift_key}")
        print(f"The decrypted quote is: {decrypted_quote}")
    else:
        print("Shift key not found.")

if __name__ == "__main__":
    main()