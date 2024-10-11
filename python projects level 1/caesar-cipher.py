# Define the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Get user inputs
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift_amount, direction):
    result_text = ""
    
    # Adjust shift for decrypting
    if direction == 'decode':
        shift_amount = -shift_amount
    
    for char in text:
        if char in alphabet:
            # Find the current index of the character
            index = alphabet.index(char)
            # Calculate the new index with wrapping around using modulo
            new_index = (index + shift_amount) % 26  # Wrap around using modulo
            # Append the new character to the result text
            result_text += alphabet[new_index]
        elif char == ' ':
            # Add a space unchanged
            result_text += ' '
        else:
            # Handle unexpected characters
            print(f"Invalid input: '{char}' is not a valid character.")
            return None  # Exit the function if invalid input is found

    return result_text

# Call the caesar function based on user input
if direction in ['encode', 'decode']:
    result = caesar(text, shift, direction)
    if result is not None:  # Only print the result if it's valid
        if direction == 'encode':
            print(f"Encrypted text: {result}")
        else:
            print(f"Decrypted text: {result}")
else:
    print("Invalid direction. Please type 'encode' to encrypt or 'decode' to decrypt.")
    
            
    
