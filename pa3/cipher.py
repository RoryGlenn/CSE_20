# assignment: programming assignment 3
# author: Rory Glenn
# date: 7/17/20
# file: cipher.py is a program that encrypts letters by using shifting the entire alphabet to the right by 3 digits
# input: give the program an input file to read such as input_file.txt
# output: writes to a new file the encrypted text and prints it to the console


"""
# encode - shift alphabet to the right by 3
def encrypt(char):
    if char < 'A' or char > 'Z' and char < 'a' or char > 'z':
        return char
    elif char >= 'A' and char <= 'Z':
        offset = ord(char) - 65
        offset = (offset + 3) % 26
        converted = offset + 65
        return chr(converted)


# decode - shift alphabet to the left by 3
def decrypt(char):
    if char < 'A' or char > 'Z' and char < 'a' or char > 'z':
        return char
    elif char >= 'A' and char <= 'Z':
        offset = ord(char) - 65
        if offset >= 3:
            offset = (offset - 3) % 26
        else:
            offset = (offset - 3) % 26
        converted = offset + 65
        return chr(converted)





check if file exist
def check_file(filename):
    try:
        filename = open(filename, mode="r+")
    except IOError:
        print(f"Error: could not find {filename}")
        return False
    return filename

"""


# encode text letter by letter using a Caesar cipher
# return a list of encoded symbols
def encode(plaintext):
    shift = 3
    ciphertext = []
    alphabet = make_alphabet()
    length = len(alphabet)

    for char in plaintext:
        found = False
        for i in range(length):
            if char == alphabet[i]:
                letter = alphabet[(i + shift) % length]
                ciphertext.append(letter)
                found = True
                break
        if not found:
            ciphertext.append(char)
    return ciphertext


# decode text letter by letter using a Caesar cipher
# return a list of decoded symbols
def decode(text):
    shift = -3
    plaintext = []
    alphabet = make_alphabet()
    length = len(alphabet)

    for char in text:
        found = False
        for i in range(length):
            if char == alphabet[i]:
                letter = alphabet[(i + shift) % length]
                plaintext.append(letter)
                found = True
                break
        if not found:
            plaintext.append(char)
    return plaintext


# read text from a file and return text as a string
def readfile(file_in):
    list_read_in = list()

    for line in file_in:
        line = line.rstrip("\n")
        for char in line:
            list_read_in.append(char.upper())

    file_in.close()
    return to_string(list_read_in)


def writefile(_list, file):
    file.write(to_string(_list))
    file.close()


# takes in a list and converts to string
def to_string(text):
    return ''.join(text)


# make a list (tuple) of letters in the English alphabet
def make_alphabet():
    alphabet = ()
    for i in range(26):
        char = i + 65
        alphabet += (chr(char),)
    return alphabet


# starting point for program
done = False

while not done:
    print("Would you like to encode or decode the message?")
    choice = input("Type E to encode, D to decode, or Q to quit: ")

    if choice == 'E' or choice == 'e':

        file_read = input("Please enter a file for reading: ")
        file_write = input("Please enter a file for writing: ")

        try:
            file_read = open(file_read, mode="r")  # why is "decrypted.txt" not being writen to???
        except IOError:
            # print(f"Error: could not find {file_read}")
            pass

        # read the file we want to encode and return a string
        file_read_str = readfile(file_read)

        # print the plaintext to console
        print("\nPlaintext:")
        print(file_read_str)

        # encode the string and return a list
        encoded_list = encode(file_read_str)

        # open the file we want to write to
        file_handler = open(file_write, "w+")  # maybe this should be r+

        # write the encoded list to the file
        writefile(encoded_list, file_handler)

        # print the ciphertext list to console
        print("Ciphertext:")
        print(to_string(encoded_list))

        file_read.close()
        file_handler.close()


    elif choice == 'D' or choice == 'd':

        file_read = input("Please enter a file for reading: ")
        file_write = input("Please enter a file for writing: ")

        try:
            file_read = open(file_read, mode="r")
        except IOError:
            # print(f"Error: could not find {file_read}")
            pass

        # read the file we want to encode and return a string
        file_read_str = readfile(file_read)

        # print the ciphertext to console
        print("\nCiphertext:")
        print(file_read_str)

        # encode the string and return a list
        decoded_list = decode(file_read_str)

        # open the file we want to write to
        file_handler = open(file_write, "w+")

        # write the decoded list to the file
        writefile(decoded_list, file_handler)

        # print the plaintext to the console
        print("\nPlaintext:")
        print(to_string(decoded_list))

        file_read.close()
        file_handler.close()

    elif choice == 'Q' or choice == 'q':
        print("\nGoodbye!")
        done = True
