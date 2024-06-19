# Write a program that takes a string input from the user and writes it to a 
# text file.

str1 = input("Enter the text you want to write in the file:")
file = open("filename.txt", 'w')
file.write(str1)
