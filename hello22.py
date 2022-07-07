class Cooking:

    def turn_n(self):
        print("hello, lets turn on the stove")
        return self

    def ingredients(self):
        print("going to the store ")
        return self

    def set_timer(self):
        print("setting the timer ")
        return self


cooking = Cooking()

cooking.turn_n().set_timer()
cooking.ingredients()

# the commands in order
# using the \ and putting all on a separate line is great for reading the code
cooking.turn_n() \
    .ingredients() \
    .set_timer()
