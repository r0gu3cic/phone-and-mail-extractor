#!/usr/bin/env python3

import re

def extract_phone_numbers(text):
    # Phone number regex
    number_pattern = re.compile(r'''
        \d{10}              # One of the ways to write a number in Serbia
        |
        \d{3}-\d{3}-\d{4}   # Another way
    ''', re.VERBOSE)
    return number_pattern.findall(text)

def extract_emails(text):
    # Email regex
    email_pattern = re.compile(r'''
        ([a-zA-Z0-9._%+-]+   # Username
        @                    # @ symbol
        [a-zA-Z0-9.-]+       # Domain name
        \.[a-zA-Z]{2,4})      # Dot-something
    ''', re.VERBOSE)
    return email_pattern.findall(text)

def main():
    text = input('Enter text with phone numbers and email addresses you want to extract:\n')

    phone_numbers = extract_phone_numbers(text)
    emails = extract_emails(text)

    if not phone_numbers:
        print('There are no phone numbers in the text')
    else:
        print('Phone numbers in the text:')
        for number in phone_numbers:
            print(number)
    print()

    if not emails:
        print('There are no e-mail addresses in the text')
    else:
        print('E-mail addresses in the text:')
        for email in emails:
            print(email)

if __name__ == "__main__":
    main()
