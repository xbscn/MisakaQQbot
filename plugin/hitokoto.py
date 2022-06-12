import json
import requests


def hitokoto(chain):
    mainurl = 'https://v1.hitokoto.cn/'
    msg = str(chain)
    typelist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    typelist2 = ['动画', '漫画', '游戏', '文学', '原创', '来自网络', '其他', '影视', '诗词', '网易云', '哲学', '抖机灵']

    try:
        types = msg.split(' ')[2]
    except IndexError:
        return '缺少参数'

    if types == '类别':
        return str(typelist2)

    try:
        code_typeindex = typelist2.index(types)
    except IndexError:
        return '无此类别'

    CodeType = typelist[code_typeindex]
    jsonstr = json.loads(requests.get(mainurl + f'?c={CodeType}').text)
    if jsonstr['from_who'] is None:
        saying = jsonstr['hitokoto'] + '----' + jsonstr['from']
    else:
        saying = jsonstr['hitokoto'] + '----' + jsonstr['from'] + ' ' + jsonstr['from_who']
    return saying
