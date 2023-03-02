def cube(x):
    return x*x*x


print(cube(5))

# but if we have list

# if we want cude of each element then we can use for loop for that


l = [1, 2, 3, 4, 5]
newl = []
for item in l:
    newl.append(cube(item))

print(newl)

# MAP

# but there is a anouther way

# we can use map function which target the each element individually
# and makes the changes
#map takes one function and the argument on which function have to be applied

newll = list(map(cube, l))
print(newll)
# but insted of cube function we can use lambda function
newl3 = list(map(lambda x:x*x*x , l))
print(newl3)


# FILTER

# filter use to filter out


def filter_function(a):
    return a > 20

# filter takes  also fun and argu
newl2 = list(filter(filter_function, newll))

print(newl2)

#filter function return either true or false 


#REDUCED
from functools import reduce
numbers = [1,2,3,4,5]
sum = reduce(lambda x,y:x+y,numbers)
print(sum)