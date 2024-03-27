def custom_function(): #Defning the custom function 
    print("HI there this the first custom function")
    print("These lines are the tasks that we wanrt to perform whenever the function is called ")

#defining the second custom function with paramerter and addition task
def custom_add(int1,int2):
    sum = int1 + int2
    print(f"The sum of the integers is {sum}")

custom_function() #calling the functions
custom_add(2,5)    