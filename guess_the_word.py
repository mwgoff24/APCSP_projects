# guess the word
import csv
import random

with open('word_list.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    word_list = []
    for row in reader:
        word_list.append(row['WORD'])
    print(word_list)

    word = word_list[0]
    print(f"Your word is: {word}.")
    word = list(word)
    print(word)

    censored_word = []
    for item in word:
        censored_word.append('*')
    print(censored_word)

    lives = 5

# game loop
while True:
    print(censored_word)
    choice = input("Do you want to guess a letter or try to solve? ")
    if choice == 'letter':
        for item in word:
            if item == choice:
                censored_word[word.index(choice)] = choice
                print("Well done! You guessed correctly!")
            else:
                print("Nope. You guessed wrong!")
                lives -= 1