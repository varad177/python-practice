# resursion
# function ke andar same function ko call krna


def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n*factorial(n-1)


print("the factorial is", factorial(4))

# recursion is process of defining something in term of itself

# fibonachhi series
# pehle 2 number ka sum


def fibonacci(n):
    if (n == 1 or n == 0 ):
        return 1
    else:

        return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(3))
