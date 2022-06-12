import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
pathDir = os.listdir("Resource/image")
for i in range(len(pathDir)):
    end=pathDir[i].split(".")[-1]
    try:
        os.rename("image/"+pathDir[i],"image/"+str(i)+"."+end)
        print("image/"+str(i)+"."+end+"已重命名")
    except:
        print(pathDir[i]+"已存在")