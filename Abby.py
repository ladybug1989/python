# Prevents a user from creating an object oof that class
# abstract class is more like a template
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation.
#abc is abstract bas class

from abc import ABC, abstractmethod

class Eater (ABC):

     @abstractmethod
     def Chef(self):
          pass


class Store_owner:
    def Chef(self):
        print("You are eating well")


class Blogger:
    def Chef(self):
        print("You are cooking ")



store_owner = Store_owner()
blogger = Blogger()



store_owner.Chef()
blogger.Chef()