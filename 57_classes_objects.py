# class is template used for creating the object


class person:
    name = "varad"
    accupation = "web-developer"
    networth = 10

    def info(self):
        print(
            f"name is {self.name} and the occupation is the {self.accupation}")
        # self parameter is the reference to te current instance of the class


# so here we creat a objects i.e "a"
a = person()
# and by using . we called the method
print(a.name)

# we can do changes by outside also
a.name = "amruta"
print(a.name)

print(a.accupation)


a.info()
