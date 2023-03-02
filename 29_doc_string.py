#doc string
#function class or module ki functionality explain krne ke liye doc string use hoti hai 
#doc string right above the fun body ke upr dalna padta hai

def squre(n):
    '''take a number n and return squre '''
    print(n**2)
    
#is tarah ham ek function me likha hua explaination ptint kr skte hai 
#ye comment nahi hoti
print(squre.__doc__)
squre(5)