# Copyright © 2021 Advaith Menon

# Permission is hereby granted, free of charge, to any person 
# obtaining a copy of this software and associated documentation 
# files (the “Software”), to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge, 
# publish, distribute, sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:

# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import random

# Constants

# For normal random password
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Large letters
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz" # Small letters
NUMBERS_CONST = "1234567890" # Allowed numbers
SPECIAL_LETTERS = "~!@#$>%^&*" # Allowed special letters
PASSWD_LEN = random.randint(10, 20) # Length of password

# For readable random password
FILE_WITH_WORDS = "words.txt" # File with words
NO_OF_WORDS = 3 # No. of words

def generate_password():
    """Generates a non-readable random password"""
    # List conversion
    upper_chars = list(UPPERCASE_LETTERS)
    lower_chars = list(LOWERCASE_LETTERS)
    num = list(NUMBERS_CONST)
    special_chars = list(SPECIAL_LETTERS)

    # Password
    passwd = ""
    for i in range(1, PASSWD_LEN + 1):
        typechooser = random.choice(["u","l","n","s"])
        if typechooser == "u":
            passwd += random.choice(upper_chars)
        elif typechooser == "l":
            passwd += random.choice(lower_chars) 
        elif typechooser == "n":
            passwd += random.choice(num) 
        elif typechooser == "s":
            passwd += random.choice(special_chars)

    return passwd

def generate_readable_password():
    """Generates a readable random password"""
    special_chars = list(SPECIAL_LETTERS)
    wordlist =[]

    with open(FILE_WITH_WORDS,"r") as file:
        # Open word
        words = file.readlines()

        for word in words:
            if len(word) > 5:
                wordlist.append(word.capitalize().split("\n")[0])
    passwd = ''
    for i in range(1, NO_OF_WORDS + 1):
        word = random.choice(wordlist)
        schar = random.choice(special_chars)
        num = str(random.randint(10, 99))
        passwd += word + schar + num

    return passwd
