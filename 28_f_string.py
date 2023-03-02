#f string
#string is used for string formating

letter = "hey my name is {} and i am from {}"
country = "india"
name = "varad"

print(letter.format(name, country))
#format me sequence dena hota hai 


#ham index bhi pass kr skte hai 
letter = "hey my name is {1} and i am from {0}"
country = "india"
name = "varad"

print(letter.format(country, name))

#now f string
country = "india"
name = "varad"
#f string me formating function use krna nahi hota hai
#direct variable de skte hai 
print(f"hey my name is {name} and i am from {country}")


txt = "for only {price:.2f} dollers"
print(txt.format(price=49.099999))



#f string bnane k liye string ke pehle f lagana jaruri hota hai  
price = 49.055
txt = f"for only {price:.3f} dollers"
print(txt)

#curly bracket as it is dena hai to 
print(f"hey my name is {{name}} and i am from {{country}}")