# an object is an instance of a class by using programming we can create and represents of real life objects a class
# can function as a blueprint that will describe what attributes and methods that are distinct  type of object will
# have created a class would write class and the name of the class

class Car:

    # the instructor that will create for us
    #is used in python as constructor. It is used to initialize the object’s state.
    # The task of constructors is to initialize(assign values) to the data members of the class when an object
    # of class is created.
    #spelling is serious  INIT
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self) :
        print("This car is driving")

    def stop(self) :
        print("This car is stopped")
