# number conversion project
# Martin Goff

# functions to define
from curses.ascii import isdigit


letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(list(letters))

def to_base_10(num, start_base):
    num_list = list(num)
    print(num_list)
    new_num_list = []
    power = len(num_list)-1
    letter_number = 10
    for item in num_list:
        if item.isdigit():
            item = int(item)
            new_item = item * (start_base ** power)
            print(f"{item}*{start_base}^{power}")
            new_num_list.append(new_item)
            power -=1
        else:
            for character in letters:
                if item == character:
                    new_item = letter_number * (start_base ** power)
                    new_num_list.append(new_item)
                else:
                    letter_number += 1

    print(new_num_list)
    print(sum(new_num_list))

def from_base_10(num, end_base):
    num = int(num)
    new_num = []
    while num // end_base != 0:
        remainder = num % end_base
        new_num.append(str(remainder))
        num //= end_base
        if num // end_base == 0:
            remainder = num % end_base
            new_num.append(str(remainder))
    new_num.reverse()
    print(new_num)
    letter_number = 10
    for item in new_num:
        if item.isdigit() and int(item) >= 10:
            item = letters.index(letters)

    print(''.join(new_num))

item_list = ["4", "E"]
for item in item_list:
    if item.isdigit():
        int(item)
        print(item)

# program loop
name = input("What is your name? ")

while True:
    num_start = input(f"What is the number you wish to convert, {name}? ")

    num_base1 = int(input(f"{name}, what base is this number in? "))

    num_base2 = int(input(f"And what is the base you wish to convert to? "))

    if num_base1 == 10:
        from_base_10(num_start, num_base2)
    elif num_base2 == 10:
        to_base_10(num_start, num_base1)
    else:
        to_base_10(num_start, num_base1)
        from_base_10(num_start, num_base2)

    proceed = input("Would you like to convert another number? y or n ")
    if proceed == 'y':
        pass
    elif proceed == 'n':
        break
    else:
        print("I don't understand this input. I guess you wanna keep going? \n")