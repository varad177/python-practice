# decorators are the functions which change the other function and return
# these are finction which takes the anouther function as anouther args


# in greet function arg is fx
# whren we write a @greet an the function it takes as a args

def greet(fx):
    def mfx(*args, **kwargs):
        print("good morning")
        fx()
        print("thanks for using this function")
    return mfx


@greet
def hello():
    print("hello world")


def add(a, b):
    print(a+b)


hello()
greet(add)(1, 2)
