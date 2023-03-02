#dictionary methods

#update method


ep1={
    111: 45,
    222:92,
    333:25,
    444:87
}

ep2={
    555:85,
    666:97
}

ep1.update(ep2);
print(ep1.items())

#clear method
ep2.clear()
print(ep2)


#empty dict
ep3={
    
}
print(ep3)

#pop method

print("pop value",ep1.pop(111))
print(ep1.items())

print(ep1.popitem())
#popteim last item ko delete kar deta hai 
print(ep1.items())

#deleteing
ep4={
    777:25,
    888:55
}
del ep4[777]
print(ep4.items())

#key provide nahi ki to puri dic delete ho jati hai