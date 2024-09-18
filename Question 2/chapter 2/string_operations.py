def separate_string(s):
    # Extract all digits from the input string
    numbers = ''.join(char for char in s if char.isdigit())
    # Extract all letters from the input string
    letters = ''.join(char for char in s if char.isalpha())
    # Return the separated numbers and letters
    return numbers, letters