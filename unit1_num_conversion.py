# number conversion project
# Martin Goff

# functions to define
def to_base_10(num, start_base):
    num_list = [int(d) for d in str(num)]
    new_num_list = []
    while len(num_list) > 0:
        for item in num_list:
            new_item = item * (start_base ** (len(num_list)-1))
            print(f"{item}*{start_base}^{len(num_list)-1}")
            print(num_list)
            new_num_list.append(new_item)
            num_list.pop(0)
    print(new_num_list)
    print(sum(new_num_list))

def from_base_10(num, end_base):
    pass


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