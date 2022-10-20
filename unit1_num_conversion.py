# number conversion project
# Martin Goff

# functions to define
from curses.ascii import isdigit

# only used if any base is larger than 10
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# to base 10, takes in a number and its base to convert to decimal
def to_base_10(num, start_base):
    # enumerates items in num
    num_list = list(num)
    new_num_list = []
    # uses -1 b/c the new num will be * by start_base ** 0 on its last digit
    power = len(num_list)-1
    letter_number = 10
    for item in num_list:
        # checks if an item in the list is a digit
        if item.isdigit():
            item = int(item)
            # multiplies item by starting base raised to a specific power, then adds to a new list
            new_item = item * (start_base ** power)
            new_num_list.append(new_item)
            power -=1
        # used if item in list is not a digit
        else:
            for character in letters:
                # loops through letters str
                if item == character:
                    #if a letter matches, letter number is reset and the loop breaks
                    new_item = letter_number * (start_base ** power)
                    new_num_list.append(new_item)
                    power -= 1
                    letter_number = 10
                    break
                # used if letter doesn't match
                else:
                    letter_number += 1
    # declared global to be used outside of function
    global new_to
    # adds the items in new_num_list for the final num, new_to
    new_to = sum(new_num_list)
    return new_to

# from base 10, takes in a number and its desired ending base to convert from decimal
def from_base_10(num, end_base):
    # int(num) b/c num is num_start, which is str
    num = int(num)
    new_num = []
    # floor division used to determine loops & conditionals
    while num // end_base != 0:
        # remainders used to get the new num
        remainder = num % end_base
        new_num.append(str(remainder))
        num //= end_base
        # used once floor division results in 0, just reruns previous code in function
        if num // end_base == 0:
            remainder = num % end_base
            # remainder is str b/c items in new_num are concatenated
            new_num.append(str(remainder))
    # reverses items in new_num
    new_num.reverse()
    for item in new_num:
        # used if item in new_num is 10 or greater
        if item.isdigit() and int(item) >= 10:
            # sets index in new_num as variable, item is removed, corresponding letter is inserted into list at specific index
            index = new_num.index(item)
            new_num.remove(item)
            new_num.insert(index, letters[int(item)-10])
    # declared global to be used outside of function
    global new_from
    # concatenates the items in new_num for the final num, new_from
    new_from = ''.join(new_num)
    return new_from


# program loop
name = input("What is your name? ")

while True:
    # asks for num, is str b/c some numbers have letters in them
    num_start = input(f"What is the number you wish to convert, {name}? ")

    # asks for current base, max is 32
    num_base1 = int(input(f"{name}, what base is this number in? "))

    # asks for base to convert to
    num_base2 = int(input(f"And what is the base you wish to convert to? "))

    # runs if current base is 10
    if num_base1 == 10:
        from_base_10(num_start, num_base2)
        print(f"\n{name}, your new number is {new_from}.")
    # runs if converted base is 10
    elif num_base2 == 10:
        to_base_10(num_start, num_base1)
        print(f"\n{name}, your new number is {new_to}.")
    # runs if not converting to or from base 10
    else:
        to_base_10(num_start, num_base1)
        from_base_10(new_to, num_base2)
        print(f"\n{name}, your new number is {new_from}.")

    # used as part of while loop if person wants to continue converting nums
    proceed = input("Would you like to convert another number? y or n ")
    if proceed == 'y':
        pass
    else:
        print("Well, you didn't say yes. Have a good day!")
        break