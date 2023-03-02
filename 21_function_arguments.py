# def average(a, b):
#     print("the average is ", (a+b)/2)


def average(a=6, b=3):
    print("the average is ", (a+b)/2)


average(5, 5)
# function me arguments hote huye bhi ye
# jidhar call kiya hai vahi ke args leta hai


average(3)
# yaha par hmne second arg pass nahi kiya to
# jo defauld argument hai vo le lega

average(b=3)
# a ki value default le lega

# is function me kitne bhi number ke skte hai


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    print("the average is ", sum/len(numbers))


average(3, 5, 7, 8, 9)


# function se ham ek value bhi return bhi le skte hai 
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    return sum/len(numbers)


c = average(10, 10, 10, 10, 10)
print("the average",c)
