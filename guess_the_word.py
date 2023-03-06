import csv

with open('word_list.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)