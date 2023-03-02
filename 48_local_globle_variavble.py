# A variable which are define in function can be used in only function
# we cannot acces this at ouitside of the function
# so this is called local variable

# but a varible which are initialise at outside of the function
# which can use in inside the function
# so this is called globle variable

x = 4
print(x)


def hello():
    x = 5
    print("local x", x)
    print("hello varad")


hello()
print("globle x ", x)


# local variable destroy when function is completed

#but if want to use local variable outside the function
# then we have to declare it as a globle


x = 11
print(x)


def hello():
    global x
    x = 22
    print("local x", x)
    print("hello varad")


hello()
print("globle x ", x)
