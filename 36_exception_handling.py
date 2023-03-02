#exeption handling

#agar error aa jyati hai code me 
#to use handle kiya jyata hai 

#unexpecter event ho handle karta hai 

a=input("enter the value: ")
print("the multiplication table of",a,"is")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    print("kindly enter the integer")
    
print("more code")