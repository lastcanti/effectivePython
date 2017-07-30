# complex expressions should be avoided
# it is much better to break expressions up  
# using helper functions

"""Create a program that asks the user to 
   enter their name and their age. 
   
   *print out a message addressed to them that tells them the 
   year that they will turn 100 years old.
"""


# we could do it this way
"""
name = input("enter name: \n")
age=input("enter age: ")
print("welcome, "+ name) 

age = (100 - int(age) ) + 2017
print("you will be 100 in the year: " + str(age))
"""

# what if we wanted to use this entire
# chunk of code again? we would create a function


def gameplay():
  name = input("enter name: \n")
  age=input("enter age: ")
  age = (100 - int(age) ) + 2017
  return(print("welcome, "+ name) + print("you will be 100 in the year: " + str(age)))
  
gameplay()
