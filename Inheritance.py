class Model:  # 1 create a class

    alive = True  # 2 a class

    # 3 create method
    def dancing(self):
        print("This model is dancing ")

    def waiting(self):
        print("This model is waiting ")


# 4 create separate classes'
# rabbit is the child class while animal is the parent class
class PlusSize(Model):
    def run(self):
        print("This Model is running ")


class AverageJane(Model):
    def excersing(self):
        print("This Average Jane is happy for her own good  ")


# 5 creating an object
plusSize = PlusSize()
averageJane = AverageJane()

print(plusSize.alive)
averageJane.excersing()
