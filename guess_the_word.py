# guess the word
import csv
import random

with open('word_list.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    word_list = []
    for row in reader:
        word_list.append(row['WORD'])

    word = word_list[0]
    print(f"Your word is: {word}.")
    word = list(word)
    word_size = len(word)
    print(word_size)

    censored_word = []
    for item in word:
        censored_word.append('*')
    print(censored_word)

    lives = 5

    # # instructions
    # print("Welcome to Guess The Word! Here, a word is picked randomly for you to guess letter by letter.")
    # print("If you guess incorrectly, you lose a life. You have five lives to start with.")
    # print("You can also solve a word by typing out the word in full.")
    # print("But be careful; if you guess the full word wrong, you lose two lives instead. \n")

    # game loop
    while True:
        print(f"You have {lives} lives currently.")
        choice = input("Do you want to guess a letter or solve? Type in l or s. ")
        if choice == 'l':
            guess = input("Guess a letter in this mystery word: ")
            for index in range(word_size):
                if word[index] == guess:
                    print(index)
                    censored_word[index] = guess
                    print(censored_word)
        elif choice == 's':
            pass
        else:
            print("That is not an available option.")