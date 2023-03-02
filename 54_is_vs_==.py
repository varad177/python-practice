# is compare the exact location of abject in memory
# == is used to compare tye values

a = 4
b = "4"
print(a is b)  # false

print(a == b)  # false

x = 5
y = 5

print(x is y)  # true

print(x == y)  # true

# so in above e.g x & y pointing exactly same memory location


p = [1, 2, 34]
q = [1, 2, 34]

print(p == q)  # true


c = None
d = None
print(c == d)  # true
print(c is None)  # true
