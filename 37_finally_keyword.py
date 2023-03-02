#finally keyword

def fun():
    try:
        l=[1,2,3,4]
        i = int(input("inter the index:"))
        print(l[i])
        return 1
    except:
        print("error occure")
        return 0
    finally:
        print("i am always executed")
        
        #finally alwayse execute hota hai 
        #agar function return bhi ho jyata hai to bhi finally execute hota hai 


fun()