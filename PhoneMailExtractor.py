#phone number and email address extractor
import re
text=input('Enter text with phone numbers and email addresses you want to extract:\n')
#phone number regex
number=re.compile(r'''
\d{10} #one of the ways to write a number in Serbia
|
\d{3}\-\d{3}\-\d{4} #another way
''',re.VERBOSE)
PhoneNumbers=number.findall(text)
#email regex
mail=re.compile(r'''(
[a-zA-Z0-9._%+-]+ # username
@ # @ symbol
[a-zA-Z0-9.-]+ # domain name
\.[a-zA-Z]{2,4} # dot-something
)''', re.VERBOSE)
Emails=mail.findall(text)
if len(PhoneNumbers)==0:
    print('There are no phone numbers in text')
else:
    print('Phone numbers in text:')
for i in range(len(PhoneNumbers)):
    print(PhoneNumbers[i])
print()
if len(Emails)==0:
    print('There are no e-mail addresses in text')
else:
    print('E-mail addresses in text:')
for i in range(len(Emails)):
    print(Emails[i])







