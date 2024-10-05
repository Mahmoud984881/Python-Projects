import random as r

# Welcome message for the game
print("Welcome to the rock-paper-scissors game!")

# Define the ASCII art for rock, paper, and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of game images for easy access
game_images = [rock, paper, scissors]

# Get the user's choice
user_choice = int(input("Please enter [0] for rock, [1] for paper, or [2] for scissors:\n"))

# Check if the user's choice is valid
if user_choice < 0 or user_choice >= 3:
    print("This entry is invalid, try again.")
else:
    # Display user's choice
    print("You chose:")
    print(game_images[user_choice])

    # Randomly select the computer's choice
    computer_choice = r.randint(0, 2)

    # Display computer's choice
    print("Computer chose:")
    print(game_images[computer_choice])

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose.")





    

    

    
    

        
    

