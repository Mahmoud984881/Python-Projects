import random as r

# Welcome message for the love measuring game
print("Welcome to the game of measuring love between you and your partner:\n")

# Get player and partner names
player_name = input("Enter your name:\n").strip().lower()
partner_name = input("Enter your partner's name:\n").strip().lower()

# Generate a random love score between 0 and 100
measuring_love = r.randint(0, 100)

# Display the love score
print(f"Your Love Score: {measuring_love}%")

def draw_heart():
    # Define the heart shape with a placeholder for the love score
    heart = [
        "  **   **  ",
        " ****** ** ",
        "***********",
        f" ** {measuring_love}% ** ",
        "  *******  ",
        "   *****   ",
        "    ***    ",
        "     *     "
    ]

    # Print each line of the heart shape
    index = 0
    if index < len(heart):
        print(heart[index])
        index += 1
    if index < len(heart):
        print(heart[index])
        index += 1
    if index < len(heart):
        print(heart[index])
        index += 1
    if index < len(heart):
        print(heart[index])
        index += 1
    if index < len(heart):
        print(heart[index])
        index += 1
    if index < len(heart):
        print(heart[index])
        index += 1
    if index < len(heart):
        print(heart[index])
        index += 1
    if index < len(heart):
        print(heart[index])

# Call the function to draw the heart
draw_heart()