# Write a program to create a base class that consists of two functions - 
# one to display a value, and another function is an abstract method. 
# Next, create a subclass that consists of a method similar to the abstract 
# method. Finally, showcase how Abstraction is being implemented in this example.
i=input("what number would you like to display?: ")
from abc import ABC, abstractmethod
class person(ABC):
    @abstractmethod
    def say(self):
        pass
class value(ABC):
    def say(self):
        print(i)
v=value()
v.say()