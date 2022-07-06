# Phone Number and Email Address Extractor
# This program allows the user to extract phone numbers
# and email addresses from a text copied to the clipboard

#! python3

import re, pyperclip

# Create phone regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?          # Separator
    (\d{3})             # First 3 digits
    (\s|-|\.)           # Separator
    (\d{4})             # Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Extension
    )''', re.VERBOSE)

# Create email regex.

emailRegex = re.compile(r'''(
    [a-zA-Z0-9.%+-]+      # Email handle
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # Domain
    (\.[a-zA-Z]{2,4})    # 'dot'-something
    )''', re.VERBOSE)

# Find matches in clipboard text.

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if (groups[8] != ''):
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
