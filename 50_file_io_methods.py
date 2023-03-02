
# readline() is use for read file line to line

f = open('varad2.txt', 'r')
i = 0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break

    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])

    print(f"marks of student {i} in sci is {m1*2}")
    print(f"marks of student {i} in math is {m2*2}")
    print(f"marks of student {i} in eng is {m3*2}")


f = open('varad3.txt', 'w')
line = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(line)
f.close()

# in above eg varad3.txt file will creat
# and by writelines the lines in array will be write in the file
