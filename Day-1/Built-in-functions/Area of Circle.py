import math #importing the python builtin function math

radius = int(input("Please enter the value of radius: ")) #converting the string input to integer value

#AOC = round(math.pi* radius**2 ,2) # math.pi is builtin function for calling the value of pi & ** is for square
#here for calculating the square of radious we can also use the built-in function pow
AOC = round(math.pi* pow(radius ,2) ,2)
print(f"The Area of the circle with {radius} is {AOC}") #Here f sting is used to combine or concatinate the string values and for good user redability