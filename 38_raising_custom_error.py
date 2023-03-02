#custom error 
#agr hame khudse error raised karni hai to ham custom error ka use kret hai 
a = int(input("enter any value between 8 & 5: "))
if (a<5 or a>8):
    raise ValueError("values should between 8 and 5")
    # app crash na ho jaye 
    # isiliye hame khudse error dene chaiye 
    
# we camn raised the error like 
  #costom
  # memory
  #stntax
  #key error