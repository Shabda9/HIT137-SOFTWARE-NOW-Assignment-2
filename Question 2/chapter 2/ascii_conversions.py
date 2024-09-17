def convert_even_numbers(num_string):
    # Convert even numbers to their ASCII decimal values
    return [ord(str(int(num))) for num in num_string if int(num) % 2 == 0]

def convert_uppercase_letters(letter_string):
    # Convert uppercase letters to their ASCII decimal values
    return [ord(char) for char in letter_string if char.isupper()]