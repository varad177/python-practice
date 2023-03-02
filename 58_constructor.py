class person:
    name = "varad"
    occ = "web-dev"

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = person()
print(a.name)

a.name = "isha"
a.occ = "HR"
a.info()
# this is how we can give the arguments
# but instead of this we can use the constructor
# for creating the constructor we have to use __init__


class person:
    def __init__(Self, n, o):
        # print("hey i am varad ")
        Self.name = n
        Self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = person("varad", "developer")
b = person("isha", "HR")
# this is how we can give args
# we can see here when we are creating object automatically constructor are calling
a.info()
b.info()
