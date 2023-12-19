import random

def hangman():
    words = ["apple", "banana", "cherry", "orange", "watermelon"]
    word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 attempts.")

    while True:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print("\n" + display_word)
        print("Guessed letters:", guessed_letters)

        if display_word == word:
            print("Congratulations! You guessed the word correctly.")
            break

        if attempts == 0:
            print("Game over! You ran out of attempts.")
            print("The word was:", word)
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts remaining.")

hangman()