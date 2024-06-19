# Write a python program that removes all punctuation from a given string

import string
 
test_str = input("Enter a string: ")
 
test_str = test_str.translate
    (str.maketrans('', '', string.punctuation))
print(test_str)