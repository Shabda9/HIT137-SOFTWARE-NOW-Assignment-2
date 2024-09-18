# The given code that have errors

# def encrypt(text, key):
#     encrypted_text =""
#     for char in text:
#         if char.isalpha():
#             shifted = ord(char) + key
#             if char.lower():
#                 if shifted > ord('z'):
#                     shifted-=26
#                 elif shifted < ord('a'):
#                     shifted += 26
#             if char.isupper():
#                 if shifted > ord('Z'):
#                     shifted-=26
#                 elif shifted < ord('A'):
#                     shifted += 26
#             encrypted_text += char(shifted)
#         else:
#             encrypted_text += char
#     return encrypted_text

# key = ???
# encrypted_code = encrypt(original_code, key)
# print(encrypted_code)

# Finding and solving the error 
def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text
    
# Using decrypt function to find the encrypted key 

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
original_code = "Hello, World! This is chapter 3 of software now assignment 2"
key = 3

# Encrypt the original code
encrypted_code = encrypt(original_code, key)
print("Encrypted Code:", encrypted_code)

# Decrypt the encrypted code
decrypted_code = decrypt(encrypted_code, key)
print("Decrypted Code:", decrypted_code)
