# number conversion project
# Martin Goff

# functions to define
def to_base_10(num, start_base):
    num_list = [int(d) for d in str(num)]
    print(num_list)
    for item in num_list:
        item * start_base ** len(num_list)
    print(sum(num_list))

def from_base_10(num, end_base):
    pass

n = 43365644
print([int(d) for d in str(n)])

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