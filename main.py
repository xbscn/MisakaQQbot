import asyncio
from asyncio import AbstractEventLoop

from graia.ariadne.app import Ariadne
from graia.ariadne.connection.util import UploadMethod
from graia.ariadne.entry import config
from graia.ariadne.event.lifecycle import ApplicationLaunched
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import MusicShare, MusicShareKind
from graia.ariadne.message.element import Plain, At, Image, Voice
from graia.ariadne.message.parser.base import MentionMe, DetectPrefix
from graia.ariadne.model import Friend, Group, Member
from graiax import silkcoder

from plugin import birthday, image, music as _music,calculator

birthdayGroups = [322819699, 599795569]
birthdayed = False
OnlyMyRailgun = MusicShare(
    kind=MusicShareKind.NeteaseCloudMusic,
    title=r"only my railgun",
    summary=r"TV动画《某科学的超电磁炮》OP1",
    jumpUrl=r"https://music.163.com/#/song?id=725692",
    pictureUrl=r"https://p1.music.126.net/pviFxK7sGSdu3xmWRt9Lgw==/109951166296227310.jpg?param=130y130",
    musicUrl=r"https://music.163.com/song/media/outer/url?id=725692.mp3",
    brief=r"",

)
app = Ariadne(
    config(
        verify_key="1034410344",  # 填入 VerifyKey
        account=934975265,  # 你的机器人的 qq 号
    ),
)


@app.broadcast.receiver(ApplicationLaunched)
async def start_background(loop: AbstractEventLoop):
    global birthdayed
    global OnlyMyRailgun
    OnlyMyRailgun_Path = "music\\fripSide (フリップサイド) - only my railgun [mqms2].mp3"
    while True:
        if birthday.isBirthday() and not birthdayed:
            for i in birthdayGroups:
                await app.send_group_message(i, MessageChain("御坂美琴生日快乐!"))
                await asyncio.sleep(1)
                await app.send_group_message(i, MessageChain(Image(path="image\\birthday.png")))
                await asyncio.sleep(1)
                await app.send_group_message(i, MessageChain([OnlyMyRailgun]))
                await asyncio.sleep(1)
                await app.send_group_message(i, MessageChain(
                    Voice(data_bytes=await silkcoder.async_encode(OnlyMyRailgun_Path, ))))
                await asyncio.sleep(1)
                with open(OnlyMyRailgun_Path, "rb") as f:
                    await app.upload_file(name="fripSide (フリップサイド) - only my railgun [mqms2].mp3", target=i, path="",
                                          data=f.read(), method=UploadMethod.Group
                                          )
            birthdayed = True
        elif (not birthday.isBirthday()):
            birthdayed = False
        await asyncio.sleep(1)


@app.broadcast.receiver("FriendMessage")
async def friend_message_listener(app: Ariadne, friend: Friend):
    await app.send_message(friend, MessageChain([Plain("Hello, World!")]))


@app.broadcast.receiver("GroupMessage", decorators=[DetectPrefix('bot 计算器')])  # 计算器
async def Calculator(app: Ariadne, chain: MessageChain, group: Group):
    if group.id == 322819699 or group.id == 599795569:
        try:
            num = calculator.calculator(chain)
            await app.send_group_message(group, MessageChain([str(num)]))
            return
        except:
            await app.send_group_message(group, MessageChain("有问题"))


@app.broadcast.receiver("GroupMessage", decorators=[DetectPrefix('bot music')])
async def music(app: Ariadne, chain: MessageChain, group: Group):  # 点歌
    if group.id == 322819699 or group.id == 599795569:  # 群判定
        text = str(chain).replace("bot music", "").strip()
        musics = _music.get(text, 3)
        try:
            await app.send_group_message(group, MessageChain(musics[0]))
            await asyncio.sleep(1)  # 防火防盗防麻花疼
            await app.send_group_message(group, MessageChain(musics[1]))
            await asyncio.sleep(1)
            await app.send_group_message(group, MessageChain(musics[2]))
        except IndexError:
            await app.send_group_message(group, MessageChain("找到的歌曲太少"))


@app.broadcast.receiver("GroupMessage", decorators=[DetectPrefix('bot ')])
async def main(app: Ariadne, chain: MessageChain, group: Group, user: Member):
    if group.id == 322819699 or group.id == 599795569:  # 群判定
        text = str(chain[1])  # 输入处理
        text = text.replace("bot ", "")
        print(text)
        await input_(app, chain, user, group, text)


@app.broadcast.receiver("GroupMessage", decorators=[MentionMe()])  # 注意要实例化
async def on_mention_me(app: Ariadne, chain: MessageChain, group: Group, user: Member):
    if group.id == 322819699 or group.id == 599795569:  # 群判定
        print(str(chain[2]).strip())  # 输入处理
        text = str(chain[2]).strip()
        await input_(app, chain, user, group, text)


async def input_(app, chain, user, group, text):
    ##input_

    if text == "贴贴":  # 贴贴
        await app.send_group_message(group, MessageChain([At(user.id), "贴贴"]))
    if text == "Misaka" or text == "misaka":  # 图片
        print("image/" + image.get())
        await app.send_group_message(group, MessageChain([At(user.id), Image(path="image/" + image.get())]))
    if text == "?":  # 帮助
        await app.send_group_message(group, MessageChain(["bot 开头或者@机器人:"
                                                          "随机御坂照片: Misaka\n"
                                                          "贴贴: 贴贴\n"
                                                          "只能bot开头"
                                                          "计算器: 计算器 <算式>(python语法)\n"
                                                          "点歌: music <音乐名>"
                                                          ]))


app.launch_blocking()
