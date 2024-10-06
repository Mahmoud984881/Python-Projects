import random

# Lists of characters to use in the password
letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")

# Get user input for the number of letters, symbols, and numbers
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize an empty list to hold the password characters
password_list = []

# Add random letters to the password list
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

# Add random symbols to the password list
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

# Add random numbers to the password list
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# Shuffle the password list to ensure randomness
random.shuffle(password_list)

# Join the characters in the password list into a single string
password = "".join(password_list)

# Display the generated password to the user
print(f"Your password is: {password}")
    

