# in python there are in build file handling function

# open takes to arguments
# first in file name & second is the mode in which file have to open
# like r->read, w-> write a->appending

f = open('vrd.txt', 'r')
# print(f)
# r mode is default

text = f.read()
# read is use for reading the file

print(text)

f.close()

# write

# f = open('varad.txt','w')
f = open('varad.txt', 'w')
# file automatically created
# f.write('the content is from write function')
# f.close()


# we can use with also

with open('varad.txt', 'a'):
    f.write('it is by with function')
