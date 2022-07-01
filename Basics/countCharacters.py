# Simple program to count the characters in a text
from os import system
import pprint, time, sys


def countCharacters(text): # Function definition
    message = text
    count = {}
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    return count

flag = True
while flag: # User input loop
    print ('Welcome to the text character counter!')
    time.sleep(0.1)
    print ('Enter your message, or (q)uit: ')
    message = input()
    if message == 'q':
        print ('Good bye!')
        time.sleep(3)
        flag = False
        system('cls')
        sys.exit
        break
    else:
       countChar = pprint.pformat(countCharacters(message))
    time.sleep(0.3)
    print()
    print()
    print ('Your message was: ' + message)
    print()
    print ('This is the count of all the characters in your message: ')
    print()
    time.sleep(0.1)
    print(countChar)
    print()
    print('-' *50)
    print()
    time.sleep(1)

