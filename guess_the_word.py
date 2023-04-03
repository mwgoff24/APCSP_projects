# guess the word
import csv
import random

# opens up large word list (over 50,000 words)
with open('word_list.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # variables to define
    attempts = 5
    gameplay = True
    word_list = []
    # adds each word in csv file to a long list
    for row in reader:
        word_list.append(row['WORD'])
    # picks a random word from the list
    word = random.choice(word_list)
    censored_word = []
    guessed_letters = []

    # functions

    # runs when player runs out of attempts
    def loss(word):
        global gameplay, attempts
        # resets lives to 0 so code does not report negative lives
        if attempts < 0:
            attempts = 0
        print(f"Oh no! You are at {attempts} attempts! The correct word was {word}. Thanks for playing!")
        gameplay = False

    # runs at beginning of program to provide user with what the game is like
    def instructions():
        print("You will start off with a censored word and must try and guess it letter by letter. \n"
        "Each incorrect guess costs one life. \n"
        "Once you think you know the word, you can try to solve it. But be warned: \n"
        "If your word is incorrect, you will lose two lives instead of one. \n"
        "When you run out of lives, your word will be revealed and the game is over. \n")

    # runs when player guesses a letter
    def letter():
        global gameplay, attempts
        letter_guess = input("\nGuess a letter in this mystery word: ")
        # catches player if they guess something they already guessed, does not penalize
        if letter_guess in guessed_letters:
            print("You already guessed this!\n")
        elif letter_guess in word:
            print("\nCorrect guess!")
            guessed_letters.append(letter_guess)
            # goes through word and appends the correct guess to each correct spot
            for index in range(word_size):
                if word[index] == letter_guess:
                    censored_word[index] = letter_guess
                    print(censored_word)
                    # used so printings of censored_word appear one at a time
                    input("\nPress ENTER:")
                    if censored_word == word:
                        # runs if player guesses every letter but does not solve word
                        print("Good job! You figured out the word! Thanks for playing!")
                        gameplay = False
        elif letter_guess not in word:
            print("Whoops! That letter is not in the word!")
            guessed_letters.append(letter_guess)
            attempts -= 1
            if attempts < 1:
                loss(''.join(word))

    # runs when player wants to solve the word
    def solve():
        global gameplay, attempts, word
        # word as a list becomes single string in order to easily check if the player's guess is correct
        word = ''.join(word)
        solve = input("Alright, then. What is the word? ")
        if solve == word:
            print("Good job! You solved the word! Thanks for playing!")
            gameplay = False
        else:
            # player loses two lives when their guess is incorrect
            print("Nope! You just lost two lives!")
            attempts -= 2
            if attempts < 1:
                loss(''.join(word))

    # setup code
    instructions()
    word = list(word)
    word_size = len(word)
    # makes identical word list except this one is censored
    for item in word:
        censored_word.append('*')
    print(censored_word)


    # game loop
    while gameplay == True:
        # every time the game loops, lives are reported to player
        # conditional below only exists to provide correct grammar at one attempt
        if attempts == 1:
            print(f"\nYou have {attempts} attempt currently.")
        else:
            print(f"\nYou have {attempts} attempts currently.")
        choice = input("Do you want to guess a letter or solve? Type in l or s. ")
        if choice == 'l':
            letter()
        elif choice == 's':
            solve()
        # catches player if they do not type in l or s (which is not uncommon)
        else:
            print("That is not an available option.")