# guess the word
import csv
import random

# opens up large word list
with open('word_list.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # variables to define
    attempts = 5
    gameplay = True
    word_list = []
    for row in reader:
        word_list.append(row['WORD'])
    word = random.choice(word_list) # will become random word after coding is finished
    censored_word = []
    guessed_letters = []
    
    # setup code
    print(f"Your word is: {word}.") # for debugging
    word = list(word)
    word_size = len(word)
    print(word_size) # for debugging
    for item in word:
        censored_word.append('*')
    print(censored_word) # this one will stay

    # functions

    def loss(word):
        global gameplay, attempts
        if attempts <= 0:
            attempts = 0
        print(f"Oh no! You are at {attempts} attempts! The correct word was {word}. Thanks for playing!")
        gameplay = False

    def letter():
        global gameplay, attempts
        letter_guess = input("\nGuess a letter in this mystery word: ")
        if letter_guess in guessed_letters:
            print("You already guessed this!\n")
        elif letter_guess in word:
            print("\nCorrect guess!")
            guessed_letters.append(letter_guess)
            for index in range(word_size):
                if word[index] == letter_guess:
                    censored_word[index] = letter_guess
                    print(censored_word)
                    advance = input("\nPress ENTER:")
                    if censored_word == word:
                        print("Good job! You figured out the word! Thanks for playing!")
                        gameplay = False
        elif letter_guess not in word:
            print("Whoops! That letter is not in the word!")
            guessed_letters.append(letter_guess)
            attempts -= 1
            if attempts < 1:
                loss(''.join(word))

    def solve():
        global gameplay, attempts, word
        word = ''.join(word)
        solve = input("Alright, then. What is the word? ")
        if solve == word:
            print("Good job! You solved the word! Thanks for playing!")
            gameplay = False
        else:
            print("Nope! You just lost two lives!")
            attempts -= 2
            if attempts < 1:
                loss(''.join(word))

    # game loop
    while gameplay == True:
        # every time the game loops, lives are reported to player
        if attempts == 1:
            print(f"\nYou have {attempts} attempt currently.")
        else:
            print(f"\nYou have {attempts} attempts currently.")
        choice = input("Do you want to guess a letter or solve? Type in l or s. ")
        if choice == 'l':
            letter()
        elif choice == 's':
            solve()
        else:
            print("That is not an available option.")