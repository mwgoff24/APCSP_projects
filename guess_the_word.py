import csv
import random

with open('word_list.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    word_list = []
    for row in reader:
        word_list.append(row['WORD'])

    word = random.choice(word_list)
    word = list(word)
    print(word)

    censored_word = []
    for item in word:
        censored_word.append('*')
    print(censored_word)