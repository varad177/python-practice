# ham is tarah tuples bana skte hai
# tuple saves multipkle item in single variable
# elements  are sepreted by commas
# enclose in round brackets
# tuple are emmutible

tup = (1, 5, 6, "varad")
print(type(tup))
print(tup)

# par  agr tuple me ek hi elemet rkhde to vo int me convert ho jyata hai
tup = (1)
print(type(tup))
print(tup)

# ek element ka tuple banane ke liye hme comma lagana padega

tup = (2,)
print(type(tup))
print(tup)

# tuple ke element change nahi ho skte
# like tup[0] = 90
# it connot change


tup = (1, 5, 6, "varad")
print(tup[3])
# baki sab list ki tarah hota hai

print("len is ", len(tup))
# length ko aise print kr skte hai

# element present hai kya nahi vo dekhne ke liye

if 6 in tup:
    print("ha present hai ")


# slicing
tub2 = tup[1:3]
print(tub2)
# tuple me ek nnew tuple creat ho jyata hai 


