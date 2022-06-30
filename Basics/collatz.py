# Program to perform the Collatz Sequence on any integer
import sys
def collatz(number):

    if (number % 2 == 0): # Check if number is even
        print (number // 2)
        return (number // 2)
    elif (number % 2 == 1): # Check if number is odd
        print (3 * number + 1)
        return (3 * number + 1)

# User Interaction

print ('Enter a number')
try:
    numberInput = int(input())
    while numberInput != 1:
        numberInput = collatz(numberInput)
except ValueError:
    print ('Please enter an integer!')
    sys.exit()




