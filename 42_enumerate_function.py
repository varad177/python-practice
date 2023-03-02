marks = [12, 34, 54, 76, 98]
index = 0
for mark in marks:
    print(mark)
    if (index == 3):
        print("good job")
    index += 1

#here we use the enumerate function
#it saves the times for making extra variables
for index,mark in enumerate(marks):
    print(index,":",mark)
    if (index == 3):
        print("good job")
    

    #we can specify the index
for index,mark in enumerate(marks, start=1):
    print(index,":",mark)
    if (index == 3):
        print("good job")