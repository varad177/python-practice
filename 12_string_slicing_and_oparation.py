# string slicing
v = 'varad,amruta,ankita'

print("the length of character is", len(v))
print(v[0:5])
print(v[6:12])
print(v[13:19])

m = 'mango'

print(m)  # pura nam print hoga
print(m[:])  # first anf last position khud lega aur pura nam print hoga
print(m[:3]) #0th position khud hi le leta hai
print(m[0:-2]) #-2 means (string size -2)
print(m[0:len(m)-2])
print(m[-3:-2]) #print only 'n'
h='harry'
print(h[-4:-2])