import datetime
def isBirthday():
    now=datetime.datetime.now()
    if now.strftime("%m%d")=="0502":
        return True
    else:
        return False
print(isBirthday())