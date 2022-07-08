# Updated version of the Multi-Clipboard program
# This version allows the user to save new strings
# to load the clipboard without modifying the source code

#! python3

''' Usage: py.exe mclip2.py save <keyword> saves clipboard content and associates it to keyword.
           py.exe mclip2.py <keyword> - Loads keyword message to clipboard.
           py.exe mclip2.py list - Loads all keywords to clipboar.
'''

import shelve, pyperclip, sys

mclipShelf = shelve.open('mclip')

# Save Clipboard content.

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mclipShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:

    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mclipShelf.keys())))
        print(str(list(mclipShelf.keys())))
    elif sys.argv[1] in mclipShelf:
        pyperclip.copy(mclipShelf[sys.argv[1]])

mclipShelf.close()
