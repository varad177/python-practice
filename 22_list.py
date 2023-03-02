# list

marks = [12, 22, 38, 22.5]
print(marks)
print(type(marks))


# python me indexing 0 se start hoti hai
print(marks[0])
print(marks[3])


# pthon me list me kuchh bhi add kr skte hai
# like  string double
l = [12, 45, "varad"]
print(l[2])
print("the len is ", len(l))


# supose hame -ve indexing di hai to
age = [12, 22, 3, 54, 67, 54, 67, 89, 87, 67, 58, 54]

print(age[-3])  # negative index
print(age[len(age)-3])  # positive index
# len se  minus krke positive me cinvert kr jyata hai
print(age[12-3])
print(age[9])


# agar koi element list me hai ya mahi ye dekhna hai to

age = [12, 22, 3, 54, 67, 54, "22"]
if 22 in age:
    print("yes")
else:
    print("no")


# 31 list me nahi hai
if 31 in age:
    print("yes")
else:
    print("no")


if "22" in age:
    print("yes")
else:
    print("no")


# ham koi word mai kuchha perticular letter hai ya nahi
# vo bhi dekh skte hai
if "ank" in "ankita":
    print("ha hai")
else:
    print("nahi hai ")


if "amu" in "amruta":
    print("ha hai ")
else:
    print("nhi hai ")

# ham list print kar skte hai
# like
age = [12, 22, 3, 54, 67, 54, 67, 58, 54]
print(age)
print(age[:])

print(age[1:])
# 1 se print karna hai to print krte smay index 1 ka element pehle aayega

print(age[2:4])
# isme index 2 se start hoga aue khatam index 5 pe hogaa


# jump indexing

age = [12, 22, 3, 54, 67, 54, 67, 58, 54]
print(age[:: 2])
print(age[1: 4])
print(age[1: 4: 2])
# 2 steps me jump hokr print karega

# list comprehension
#list ko generate krna 


lst =[i*i for i in range(10)]
print(lst)
#ham list me condition bhi dal skte hai 
lst =[i for i in range(10) if(i%2==0)]
print(lst)
