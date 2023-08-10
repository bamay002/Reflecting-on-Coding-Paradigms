# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to FPP

def flatten_and_sort(array):
    arr=[]
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)


# How does this solution ensure data immutability?
'''
This solution doesn't ensure data immutability because data immutability means the  information within a database
cannot be deleted or changed and the .append allows for items to be added.
'''
# Is this solution a pure function?
'''
No, this solution is not a pure function. Pure function means a function always returns the same result if the
same arguements are passed. Since we have the arr  which modifies the array and performs sorting
'''
# Is this solution a high order function?
'''
No, this solution is not a high order function. A high order function is a function that takes one or more functions 
as arguments, or returns a function as its result. Our function above doesn't take or return any functions, it just
deals with arrays.
'''
# Would it have been easier to solve this using a different programming style?
'''
I think we could have used a more function programming style to make it a bit easier to solve.
'''
# Why in particular is function programming a helpful paradigm when solving this problem?
'''
Functional programming is a helpful paradigm when solving this problem because function programming is better at 
making the code consise and readable. 
'''

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


# Implement a function using an Object Oriented Solution
    # First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
    # Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def boost(self):
    self.max_speed *= 2
    
    # Define another class that inherits Podracer and call this one SebulbasPod. 
    # This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def flame_jet(self,other):
    other.condition = "trashed"

# How does this solution demonstrate the four pillars of OOP?
'''
 - encapsulation: demonstrated through attributes such as max_speed, condition, price within Podracer, AnakinsPod, SebulbasPod classes
 - abstraction: demonstrated through objects
 - inheritance: demonstrated through the classes AnakinsPod and SebulbasPod
 - polymorphism: demonstrated through the boost method and flame_jet method
'''
# Would it have been easier to implement a solution to this problem using a different coding style?
'''
I think the use of OOP was a good approach for solving this problem
'''
# How in particular did OOP assist in the solving of this problem?
'''
OOP assisted in solving this problem by being organized such as the use of classes, and objects which made it easier to manage
OOP also adds new features without affecting the exisitng code
'''