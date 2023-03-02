tup = (12, 34, 54, 67, 55)
print(tup)

# tuple  ke liye koi method nahi hote
# agar method applied krne hai to usko pehle list me
# convert krna pdega badme list ke method ham applied kr skte hai

# upr ke tuple me agar add krna hai to

list = list(tup)
list.append(100)
tup = tuple(list)
print(tup)

# is tarah ham list ke sare method use  kr skte hai


# tuple me kitme elements hai vp ham calculate kr skte hai 

tup = (23,54,67,45,54,54)
count = tup.count(54)
print(count)

# index   
index=tup.index(23)
print(index)