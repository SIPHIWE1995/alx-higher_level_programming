#!/usr/bin/python3
first_num = 97
last_num = 123
"""Print the alphabet in lowercase, not followed by a new line."""
for alphabets in range(first_num, last_num):
    print("{}".format(chr(alphabets)), end="")
