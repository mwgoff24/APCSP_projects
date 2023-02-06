# encryption project
# Martin Goff

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

shift = input("How much do you want to shift by? ")

for item in letters:
    new_index = letters.index(item)+int(shift)
    if new_index > 25:
        new_index -= 26
    print(letters[new_index])

unusable_chars = "/.,?';:!)("
unusable_list = list(unusable_chars)

def encrypt():
    index = int(input("What do you want your index to be? Type in a number. "))
    message = input("What is the message you want to use? ")
    message_list = list(message.lower())
    for character in message_list:
        if character in unusable_chars:
            message_list.remove(character)
    new_letters = letters
    for character in message_list:
        if character in letters:
            letters.index(character)+index
    print(message_list)



while True:
    encrypt_or_decrypt = input("Do you want to encrypt or decrypt some text? e/d: ")
    if encrypt_or_decrypt == 'e':
        encrypt()
    elif encrypt_or_decrypt == 'd':
        index = input("What do you want your index to be? Type in a number. ")
        message = input("What is the message you want to use? ")
    else:
        print("I believe that is not an option.")