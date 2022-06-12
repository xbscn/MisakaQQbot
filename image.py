import random,os


def get():
    pathDir = os.listdir("image")  # 取图片的原始路径
    sample = random.choice(pathDir)
    return sample