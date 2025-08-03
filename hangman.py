import random

word_list = ["apple", "zebra", "piano", "dream", "storm"]
def choose_word():
    return random.choice(word_list)

def show_intro():
    print("Welcome to Hangman Game!")
    print("Guess the word one letter at a time.")
    print("You have 6 chances. Let's go!\n")
def play_game():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_guesses = 6

    while incorrect_guesses < max_guesses:
        # Display progress
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(f"\nWord: {display_word}")

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print(" Already guessed that letter.")
        elif guess in word:
            print(" Correct guess!")
            guessed_letters.append(guess)
        else:
            print(" Incorrect!")
            incorrect_guesses += 1
            guessed_letters.append(guess)

        if all(letter in guessed_letters for letter in word):
            print(f"\n You guessed the word: {word}!")
            break

    if incorrect_guesses == max_guesses:
        print(f"\n Game Over! The word was: {word}")
def play_again():
    while True:
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again == 'y':
            play_game()
        elif again == 'n':
            print(" Thanks for playing!")
            break
        else:
            print("Please enter y or n.")
show_intro()
play_game()
play_again()        