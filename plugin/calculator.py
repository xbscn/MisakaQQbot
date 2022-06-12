def calculator(chain):
    text = str(chain).replace("bot 计算器", "").strip()
    can = "1234567890+-*/()|&^."
    canfun = ["sum"]  # 当作没有
    indexOffest = 0  # 当作没有
    for i in range(len(text)):
        i += indexOffest  # 当作没有
        _break = False
        if (text[i] in can):

            pass
        else:  # 放弃兼容sum 当作没有
            for i2 in canfun:
                print(f"off:{indexOffest},i2:{i2},i1{text[i]}")
                if text[i:i + len(i2)] in canfun:

                    indexOffest += len(i2)
                    pass
                else:
                    _break = True
                    break
            if (_break):
                break
    else:
        try:
            num = eval(text)
        except Exception as e:
            num = e