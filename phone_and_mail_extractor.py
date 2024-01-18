#!/usr/bin/env python3

# Phone number and email address extractor
import re
text=input('Enter text with phone numbers and email addresses you want to extract:\n')
# Phone number regex
number=re.compile(r'''
\d{10} # One of the ways to write a number in Serbia
|
\d{3}\-\d{3}\-\d{4} # Another way
''',re.VERBOSE)
phone_numbers=number.findall(text)
# Email regex
mail=re.compile(r'''(
[a-zA-Z0-9._%+-]+ # Username
@ # @ symbol
[a-zA-Z0-9.-]+ # Domain name
\.[a-zA-Z]{2,4} # Dot-something
)''', re.VERBOSE)
emails=mail.findall(text)
if len(phone_numbers)==0:
    print('There are no phone numbers in the text')
else:
    print('Phone numbers in the text:')
for i in range(len(phone_numbers)):
    print(phone_numbers[i])
print()
if len(emails)==0:
    print('There are no e-mail addresses in the text')
else:
    print('E-mail addresses in the text:')
for i in range(len(emails)):
    print(emails[i])





