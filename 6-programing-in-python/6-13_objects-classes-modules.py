#vectors
class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, other):
         return Vector(self.x + other.x, self.y + other.y)

#puzzlebox
def answer(puzzlebox):
    return 42

#quarks
class Quark(object):
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
        
    baryon_number = 1/3
    
    def interact(self, other_quark):
        self.color, other_quark.color = other_quark.color, self.color

#######################################
#full puzzlebox class list
import random


class Puzzlebox(object):
    """Puzzlebox for codewars kata."""

    def __init__(self):
        self.key = random.randint(1, 99)

    answer = "Ha, not quite that easy.\n"

    hint = "How do you normally unlock things?\n"
        
    hint_two = "The lock attribute is a method. Have you called it with anything yet?\n"

    def lock(self, *args):
        if len(args) != 1:
            return "This method expects one argument.\n"
        elif type(args[0]) != int:
            return "This method expects an integer.\n"
        elif args[0] != self.key:
            return "Did you know the key changes each time you print it?\n"
        else:
            return "You put the key in the lock! The answer is, of course, 42. Return that number from your answer() function to pass this kata.\n"

    def __repr__(self):
        return "The built-in dir() function is useful. Continue adding print statements till you know the answer.\n"

puzzlebox = Puzzlebox()

##    print(dir(puzzlebox))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', 
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
# '__subclasshook__', '__weakref__', 'answer', 'hint', 'hint_two', 'key', 'lock']

##   print(type(puzzlebox))
# <class 'setup.Puzzlebox'>

##  print(puzzlebox.key)
# 82