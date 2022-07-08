# duck typing = concept where the class of an object is less important than the methods
# class type is not checked is not checked if minimum methods/attributes are present
# if it walks like a duck, it's a duck concept

class Duck:

    def walk(self):
        print("This  chicken is walking ")

    def talk(self):
        print("This chicken is clucking ")


class Chicken:

    def walk(self):
        print("This  chicken is walking ")

    def talk(self):
        print("This chicken is clucking ")


# trying to catch a duck in this class

class Person():

    def catch (self, duck):
        duck.walk()
        duck.talk()
        print("You caught the duck ")


duck = Duck()
chicken = Chicken()
person = Person()

# to catch argument have to use the person
# once it has the same attributes it will work 

person.catch(duck)
person.catch(chicken)