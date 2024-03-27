#Write a program that calculates the factorial (!) of any given number by a user
import math
num = int(input("Please enter the number for calculating the factorial\n " ))

factorial = math.factorial(num)

print(f"The factorial for the {num} is {factorial}")

