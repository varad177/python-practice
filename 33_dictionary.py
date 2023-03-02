#dictionary
#the store multiple elements in single variable
dic={
    "varad": "human being",
    "mouse":"object"
}


# dictionary is used to store thr information 
#which can access by direct indexing
print(dic)
print(dic["varad"])

print(dic["mouse"])



#storing the id of employee in dic
id={
    121:"varad",
    124:"isha",
    868:"aditya",
    586:"mayur",
    "eligible":True
}

print(id)

print(id[121])

print(id.get("eligible"))

#ye syntx error throw nahi karta hai 
print(id.get("sneha"))

#all keys access krne ke liye 
print(id.keys())

for key in id.keys():
  print(f"the value corresponding to the key {key}is{id[key]}")
    
#all values print krne ke liye 
print(id.values())

for value in id.values():
    print("=>",value)


#use of item

print(id.items())

for key, value in id.items():
    print(f"key is {key}, value is {value}")