import requests

url = "https://v0.yiketianqi.com/api?unescape=1&version=v91&appid=64534918&appsecret=2pBVQ2bQ&ext=&cityid=&city={}"
city = "新化"


def get(city):
    r = requests.get(url=url.format(city))
    try:
        if r.json()["errcode"]==100:
            return "未知城市"
    except:
        print("未知城市")
    data = r.json()["data"]
    return ("{}:\n".format(city) +
            "天气:{}".format(data[0]["wea"]) +
            "{}℃\t{}~{}℃".format(data[0]["tem"], data[0]["tem1"], data[0]["tem2"]))
