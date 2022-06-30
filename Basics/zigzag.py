# This program prints a back-and-forth zigzag pattern
# to the console untile the user stops the program execution

from os import system
import time, sys

indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # Main program loop.
        print(' ' * indent, end='')
        print('**********')
        time.sleep(0.01) # Pause

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 10:
                # Change direction
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent =  indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True

except KeyboardInterrupt:
    system('cls')
    sys.exit()
