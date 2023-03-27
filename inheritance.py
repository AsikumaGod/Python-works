# i am testing how imheritance works
class Test():
    def master(self):
        print("it works")


class Slave(Test):
    def __init__(self, name):
        self.name = name

    def namelog():
        print(f"as, {self.name}")


first_test = Slave('Kofi')
first_test.namelog()
