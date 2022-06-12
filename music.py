import requests
import json
import pickle

from graia.ariadne.message.element import MusicShare, MusicShareKind

data = {"s": "water", "limit": 2}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
with open("cookies.pickle", "rb") as f:  # 实际上根本不需要，只要随便一个字符串当电话就行
    se = pickle.load(f)


def get(s, limit):
    global se

    musics = []
    text = ""
    url = "http://music.163.com/api/search/pc/?type=1&s={}&limit={}".format(s, limit)  # 获取列表
    r = se.get(url=url, headers=headers)
    page = r.json()
    songs = page['result']['songs']  # json解析
    print(songs)
    for i in songs:
        artists = ""
        for i2 in i['artists']:  # 如果多个作者就放在一起
            artists += i2["name"] + " "
        Music = MusicShare(MusicShareKind.NeteaseCloudMusic, i["name"], artists,
                           "https://music.163.com/#/song?id={}".format(str(i["id"])), i['album']['blurPicUrl'],
                           "http://music.163.com/song/media/outer/url?id={}.mp3".format(str(i["id"])), "")
        musics.append(Music)
    return musics
