import os
pathDir = os.listdir("image")
for i in range(len(pathDir)):
    os.rename("image/"+pathDir[i],"image/"+str(i)+"."+pathDir[i][-3:len(pathDir[i])])