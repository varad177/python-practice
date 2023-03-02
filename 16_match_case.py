x = int(input("enter the value of x: "))
match x:
    case 0:
        print("the x is zero")

    case 4:
        print("the x is 4")

   
    case _ if(x!=90):
        print(x ,"is not equl to 90")
   
    case _:
        print("the default value is :", x)

  

        # it is like swith case
        # but isme break nahi hota 
