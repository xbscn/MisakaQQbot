import random,os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
def get():
    pathDir = os.listdir("Resource/image")  # 取图片的原始路径
    sample = random.choice(pathDir)
    return sample