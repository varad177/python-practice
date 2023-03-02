# seek()
# tell()

# in python seek(), and tell() functions are used to work
# with file object and their positions within a file

with open('varad4.txt', 'r') as f:
    print(type(f))

    f.seek(3)
    # seek is used for changing the starting point

    print(f.tell())
    # tell is used for getting the seek value

    data = f.read(5)
    # only 5 character will be read
    print(data)


# truncate
#truncate is used for deciding the size of the file 

with open('varad5', 'w') as f:
    f.write("hello varad")
    f.truncate(5)
    #Olnly 5 character will br store

with open('varad5.txt', 'r') as f:
    print(f.read())
