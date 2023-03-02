set1 = {10, 2, 5, 6}
set2 = {2, 7, 5, 9}

print(set1, set2)

# union
print("union")
print(set1.union(set2))

# intersection
print("inter-section")
print(set1.intersection(set2))
print(set2.intersection(set1))

print("after updating")
set1.update(set2)
''
# set me set2 ki values chali jayegi
print(set1, set2)

s1 = {10, 2, 5, 6}
s2 = {2, 7, 5, 9}

s1.intersection_update(s2)
print(s1)

s1 = {10, 2, 5, 6}
s2 = {2, 7, 5, 9}


print("symmitric difference/uncommon value")
s3 = s1.symmetric_difference(s2)
print(s3)

print("difference")
s1 = {10, 2, 5, 6}
s2 = {2, 7, 5, 9}
s3 = s1.difference(s2)
print(s3)


print("is-disjoint/no common element")
s1 = {10, 5, 6}
s2 = {2, 7, 9}
print(s1.isdisjoint(s2))

print("super-set")
s1 = {2, 10, 7, 5, 9, 6}
s2 = {2, 7, 9}
print(s1.issuperset(s2))

print("addint element")
s1 = {5, 6, 7}
s1.add("varad")
print(s1)


print("removing element")
s1.remove("varad")
print(s1)

print("discarding element")
# discard can give error
s1.remove(6)
print(s1)

print("poping elements")
s1 = {5, 6, 7,"varad"}
item =s1.pop()
print(item)

s1 = {5, 6, 7}

# del s1
# del use to delete set

print("clearing element")
s1.clear()
s1.add("varad")
print(s1)

name={"varad","amu","ankita"}
if "ankita" in name:
    print("ankita is present in set")
else:
    print("ankita is not present ")
