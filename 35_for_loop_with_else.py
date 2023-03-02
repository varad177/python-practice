#for loop with else 


for i in range(1,5):
    print(i)

else:
    print("out of for loop")
    
    #empty loop
for i in []:
    print(i)

else:
    print("out of for loop")
    
    
#loop khatam hone ke bad ho else execute hota hai 
#loop agar bich me break ho jyata hai to else execute mahi hoga 
i=0
while(i<=8):
    print(i)
    i=i+1
    
else:
    print("out for while loop")