#!/usr/local/bin/python3

import argparse

def encrypt(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        elif (char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result

parser = argparse.ArgumentParser(description='Encrypt and decrypt messages!')
parser.add_argument('direction')
parser.add_argument('message')
parser.add_argument('offset', type=int)

args = parser.parse_args()

if args.direction=='encrypt':
    result = encrypt(args.message, args.offset)
elif args.direction=='decrypt':
    result = encrypt(args.message, -1*args.offset)
    
print("Message: ", args.message)
print("Offset : ", args.offset)
print("Result : ", result)

