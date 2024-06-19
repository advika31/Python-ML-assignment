# Write a program that asks the user for their birth year and calculates their 
# age

year = int(input("Enter birth year: "))

if (year < 2024):
    age = 2024 - year
    print("Your age is", age)
    
else :
    print("Invalid year")
