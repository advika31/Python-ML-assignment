# Write a python program that calculates the factorial of a given number.

a = int(input("Enter a number:"))
fact = 1
for i in range (1, a+1):
    fact = fact*i
print("Factorial of", a, "is:", fact)