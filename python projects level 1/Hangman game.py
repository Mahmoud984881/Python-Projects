import random

# Hangman stages
stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Word list
hangman_words = [
    "apple", "banana", "orange", "grape", "cherry", "pineapple", "strawberry", "watermelon", 
    "lemon", "mango", "computer", "python", "programming", "game", "hangman", "language", 
    "development", "software", "algorithm", "function", "variable", "internet", "database", 
    "science", "technology", "basketball", "football", "baseball", "tennis", "volleyball", 
    "hockey", "golf", "swimming", "running", "cycling", "hiking", "travel", "adventure", 
    "music", "painting", "drawing", "sculpture", "photography", "theater", "literature", 
    "history", "geography", "mathematics", "physics", "chemistry", "biology", "psychology", 
    "philosophy", "sociology", "economics", "politics", "government", "culture", "tradition", 
    "religion", "spirituality", "mindfulness", "meditation", "wellness", "health", "fitness", 
    "nutrition", "cooking", "baking", "gardening", "nature", "environment", "sustainability", 
    "ecology", "conservation", "wildlife", "ocean", "mountain", "river", "forest", "desert", 
    "island", "city", "town", "village", "community", "family", "friendship", "love", 
    "happiness", "success", "motivation", "inspiration", "creativity", "innovation", 
    "education", "learning", "knowledge", "wisdom", "legacy"
]

# Choose a random word
chosen_word = random.choice(hangman_words)
word_length = len(chosen_word)
lives = 6

# Create blanks
display = ['_' for _ in range(word_length)]

# Game slogan and introduction
print("Welcome to Hangman!")
print("Challenge yourself in the game of Hangman! Discover the words before you run out of lives.")


# Game loop
while lives > 0 and '_' in display:
    print(stages[lives])  # Display the current hangman stage
    print(f"Current word: {' '.join(display)}")  # Show current state of the word
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed '{guess}'. Try again.")
        continue  # Skip the rest of the loop if the letter was already guessed

    # Check guessed letter
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
        print(f"Good job! '{guess}' is in the word.")
    else:
        lives -= 1
        print(f"Sorry, '{guess}' is not in the word. You lose a life.")

# End of game messages
if '_' not in display:
    print("Congratulations! You've guessed the word:", chosen_word)
else:
    print(stages[0])  # Show the last stage of the hangman
    print("You lose. The word was:", chosen_word)

