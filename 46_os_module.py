# build in module
# use for automisation
# like for deleting file , creating file and so on

import os
# agar data folder exist nahi karta to
# to data folder creat hoga
# if (not os.path.exists("data")):
#     os.mkdir("data")


# nahi to i wala loop se data me folders creat ho jayenge
# for i in range(0, 100):
    # os.mkdir(f"data/day{i+1}")
    # os.rename(f"data/day{i+1}",f"data/tutorial {i+1}")
    # os.rename(f"data/tutorial{i+1}",f"data/tutorial {i+1}")

    #rename use for rename the folders
    

folders = os.listdir("data")
for fol in folders:
     print(fol)


# os.remove("data/tutorial 1")


#explore other os functions