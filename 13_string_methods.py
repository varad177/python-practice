v = 'Varad'
print("original string::- "+v)

print("length")
print(len(v))
print(v.upper())
print(v.lower())
# string are emmutible in python
a = '!amruta!!!!!!!!!'
print(a.rstrip("!"))

print("replace")
print(a.replace("amruta", "varad"))


print("split")
aa = 'ankita amruta varad'
# split method ek list banata hai
print(aa.split(" "))
l = "hello laki"
print(l.capitalize())


print("centre method")
b = "welcome to my house"
print(b.center(50))
print(len(b))
print(len(b.center(50)))

print("count")
an = "how are u varad, where are u varad"
print("no of varad in given string is", an.count("varad"))

print("str end switch")
x = "hii amruta !!"
print(x.endswith("!!"))

print("find")
z = "there is a zebra"
print("first accurance of 'is' is", z.find("is"))

print("isalnum, A-Z, a-x, 0-9, se bani string")
n="varad142"
print(n.isalnum())

print("is alpha method")
f="forest"
print(f.isalpha())
g="joker45"
print(g.isalpha())

print("is alpha")
v="varad"
print(v.islower())
v="vArad"
print(v.islower())

print("is string prrintable")
v="varad\n"
print(v)
print(v.isprintable())

print("title")
v="hello varad, hii"
a=v.title()
print(a) #converting in title

print("checking title")
print(a.istitle())

print("swao case")
v="hII, VaRaD"
print(v.swapcase()
)