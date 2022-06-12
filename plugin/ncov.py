import requests

url = "https://lab.isaaclin.cn/nCoV/api/area?province={}"


def get(province):
    text = ""
    r = requests.get(url.format(province))
    if r.json()["results"]==[]:
        return "未找到省份哦~是不是忘记加-省了"
    print(r.json()["results"])

    r = r.json()["results"][0]["cities"]
    for i in r:
        text += ('城市:{}\t'.format(i["cityName"]) +
                 "现有确诊:{}\t".format(i["currentConfirmedCount"])+
                 "累计确诊:{}\t".format(i["confirmedCount"])+
                 "疑似病例:{}\t".format(i["suspectedCount"])+
                 "治愈:{}\t".format(i["curedCount"])+
                 "死亡:{}\n".format(i["deadCount"])
                 )
    return text

