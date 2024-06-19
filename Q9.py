# Write a python program that checks if a substring is present in a given 
# string

str1 = input("Enter main string:")
str2 = input("Enter substring:")

if str2 in str1:
    print("Substring is present")
else:
    print("Substring is not present")