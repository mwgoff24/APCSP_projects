# encryption project
# Martin Goff

# this project takes a message provided by the user and either encrypts or decrypts it.
# if there is a symbol on the keyboard, it can run through the program, but only letters are affected by the code.
# encryption and decryption are triggered by user input; either e or d is entered to trigger its respective function.
# both functions are the same except decryption moves to the left in the letters list and encryption moves right.

# global variables
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
special_chars = " 1234567890!@#$%^&*)(-_=+/?.>,<`~][}{\|"

# functions

# encrypt, asks for a shift, takes a message, shifts every letter the requested amount
def encrypt():
    shift = int(input("\nHow much do you want your shift to be? Type in a number. "))
    message = input("\nWhat is the message you want to use? ")
    # makes all letters lowercase for easier code
    message_list = list(message.lower())
    new_message_list = []
    for character in message_list:
        if character in letters:
            # this variable is the letter's index in the letters list, which has the shift added next
            placement = letters.index(character)
            placement += shift
            # error handling if shift goes out of range
            if placement > 25:
                placement -= 26
            new_message_list.append(letters[placement])
        # space counts as a special character, function only adds these characters and does not do anything to them
        if character in special_chars:
            new_message_list.append(character)
    # print statement joins the list into a single string
    print(f"\nYour encrypted message is: {''.join(new_message_list)}")


# decrypt, same as decrypt but goes the opposite direction
def decrypt():
    shift = int(input("\nHow much do you want your shift to be? Type in a number. "))
    message = input("\nWhat is the message you want to use? ")
    message_list = list(message.lower())
    new_message_list = []
    for character in message_list:
        if character in letters:
            placement = letters.index(character)
            placement -= shift
            # more error handling
            if placement < 0:
                placement += 26
            new_message_list.append(letters[placement])
        if character in special_chars:
            new_message_list.append(character)
    print(f"\nYour decrypted message is: {''.join(new_message_list)}")

# loop
while True:
    # program asks user to encrypt or decrypt
    encrypt_or_decrypt = input("\nDo you want to encrypt or decrypt some text? e/d: ")
    if encrypt_or_decrypt == 'e':
        encrypt()
    elif encrypt_or_decrypt == 'd':
        decrypt()
    else:
        print("\nI believe that is not an option.")