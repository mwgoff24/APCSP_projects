# guess the word
import csv
import random

# opens up large word list
with open('word_list.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # variables to define
    lives = 5
    points = 0
    word_list = []
    for row in reader:
        word_list.append(row['WORD'])
    word = word_list[0] # will become random word after coding is finished
    censored_word = []
    
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
        if lives <= 0:
            lives = 0
        print(f"Oh no! You now have {lives} lives! The correct word was {word}.")


    # # instructions
    # print("Welcome to Guess The Word! Here, a word is picked randomly for you to guess letter by letter.")
    # print("If you guess incorrectly, you lose a life. You have five lives to start with.")
    # print("You can also solve a word by typing out the word in full.")
    # print("But be careful; if you guess the full word wrong, you lose two lives instead. \n")

    # game loop
    while True:
        # every time the game loops, lives are reported to player
        print(f"You have {lives} lives and {points} points currently.")
        choice = input("Do you want to guess a letter or solve? Type in l or s. ")

        if choice == 'l':
            letter_guess = input("Guess a letter in this mystery word: ")
            if letter_guess in word:
                print("Correct guess!")
                for index in range(word_size):
                    if word[index] == letter_guess:
                        censored_word[index] = letter_guess
                        print(censored_word)
                        advance = input("Press ENTER:")
                        points += 100
            elif letter_guess not in word:
                print("Whoops! That letter is not in the word!")
                lives -= 1
                if lives <= 1:
                    loss(''.join(word))

        elif choice == 's':
            word = ''.join(word)
            solve = input("Alright, then. What is the word? ")
            if solve == word:
                points += 1000
                print("Good job! You guessed the word!")
            else:
                print("Nope! You just lost two lives!")
                lives -= 2
                if lives <= 1:
                    loss(''.join(word))

        else:
            print("That is not an available option.")