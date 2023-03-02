# function

# kuch build in function bhi hote hai 
# min(), max(), len(), sun(), type(), range(), dict(),
# list(), tuple() set(), print(), etc

a = 9
b = 8
gmean = (a*b)/(a+b)
print(gmean)
if (a > b):
    print("first number is greater")
else:
    print("second number is greater")


a = 10
b = 8
gmean = (a*b)/(a+b)
print(gmean)


# yaha par hmne  ek function banaya
# function banane ke liye  def likhna jaruri hota hai

def calculategmean(a, b):
    gmean = (a*b)/(a+b)
    print(gmean)
    isgrater(a, b)
    # is tarah ham function me function bhi use kr skte hai


def isgrater(a, b):
    if (a > b):
        print("first number is greater")
    else:
        print("second number is greater")


# yaha  par hne ek function likha
# jisme kuchh likha nahi hai
# isiliye error nahi chahiye to
# hame pass likhna padega
# function ham badme use krte skte hai
def islesser(a, b):
    pass


a = 9
b = 8
calculategmean(a, b)
# yaha hamne upar wala function use kiya

a = 10
b = 11
calculategmean(a, b)
