#! python3
'''This program accepts a street address from the command line
or from user input and opens the Google Maps page for the
address'''

import sys, webbrowser

if len(sys.argv) > 1:
    # Get the address from the command line.
    address = ' '.join(sys.argv[1:])

else:
    # Get address from the user.
    print('Please enter the address you want to search for:')
    address = input()

webbrowser.open('https://www.google.com/maps/place/' + address)
