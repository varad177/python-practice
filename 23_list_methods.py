l=[1,2,3,5,6,4]
print(l)


# list ki length find krni hai to 
# len means  number of elements 
len = len(l)
print("the length is ",len)


# list ke end me element add krna hai to
l.append(9)
print(l)

# list sort krne ke liye
list = [23,43,57,3,678,53,98]
print("original list is ", list)
list.sort()
print("sorted list is ", list)

# agar descending order me print krna hai to 
list = [23,43,57,3,678,53,98]
print("original list is ", list)
list.sort(reverse=True)
print("sorted descending list is ", list)

# list ko reverse krne ke liye 
list = [23,43,57,3,678,53,98]
list.reverse()
print("reverse list is ", list)

# lisi element ki index find krni ho to 
list = [23,43,57,3,68,53,98]
print("index is ",list.index(53))

# list me element kitni bar aa rha hai to find krne ke liye 
list = [23,57,57,3,68,57,98]

print("the count is ",list.count(57))

# list ko agr copy krna hai 
list = [23,57,57,3,68,57,98]
m=list.copy()
print("the copied list is ",m)


# ahe kisi index pr insert karna hai 
list.insert(1,100)
print("the list by indexing ",list)

# extend method 

list = [23,57,57,3,68,57,98]
mar = [900,1000,1100]
# mar list open hogi aur list me end me jud jayegi

list.extend(mar)
print("the entended list is ",list)



# list ko joined bhi kr skte hai 
age =[1,2,3]
num=[11,12,13]
list = age+num
print("the connected list is ", list)
