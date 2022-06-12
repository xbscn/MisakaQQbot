import os
pathDir = os.listdir("image")
for i in range(len(pathDir)):
    end=pathDir[i].split(".")[-1]
    try:
        os.rename("image/"+pathDir[i],"image/"+str(i)+"."+end)
        print("image/"+str(i)+"."+end+"已重命名")
    except:
        print(pathDir[i]+"已存在")