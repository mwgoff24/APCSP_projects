# encryption project
# Martin Goff

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# shift = input("How much do you want to shift by? ")

# for item in letters:
#     new_index = letters.index(item)+int(shift)
#     if new_index > 25:
#         new_index -= 26
#     print(letters[new_index])

unusable_chars = "/.,?';:!)("
unusable_list = list(unusable_chars)

def encrypt():
    global letters
    shift = int(input("How much do you want your shift to be? Type in a number. "))
    message = input("What is the message you want to use? ")
    message_list = list(message.lower())
    for character in message_list:
        if character in unusable_chars:
            message_list.remove(character)
        if character in letters:
            placement = letters.index(character)
            placement += shift
            message_list.insert(message_list.index(character), letters[placement])
        print(message_list)


def decrypt():
    pass


while True:
    encrypt_or_decrypt = input("Do you want to encrypt or decrypt some text? e/d: ")
    if encrypt_or_decrypt == 'e':
        encrypt()
    elif encrypt_or_decrypt == 'd':
        decrypt()
    else:
        print("I believe that is not an option.")