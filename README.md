# Simple Password Generator
A simple password generator, written in Python
## How to use the tool
First import the module: `from random_password import generate_password, generate_readable_password`. Then call the function `generate_password()`. It will return the password as a string
## Setting length of passwords, no. of words in readable passwords etc.
In the file `random_password.py`, modify the following constants to do the same:
Constant | Type | Value
---------|------|------
SPECIAL_LETTERS | str | Choose the special letters that appear in your password. For example, you can add/remove certain characters.
PASSWD_LEN | int | The length of the non readable password. By default it is a random number between 10 and 20. You can change the limit. **Note:** On most websites, the minimum number of characters required are 8 and the maximum allowed is 32.
FILE_WITH_WORDS | str | A .txt file with the words. Only one word must be there in each line. I used http://gwicks.net/dictionaries.htm for the list.
NO_OF_WORDS | int | The number of words in a readable password.
