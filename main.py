from graia.ariadne.app import Ariadne
from graia.ariadne.entry import config
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain, At, Image
from graia.ariadne.message.parser.base import MentionMe, DetectPrefix
from graia.ariadne.model import Friend, Group, Member
import random
import image

app = Ariadne(
    config(
        verify_key="1034410344",  # 填入 VerifyKey
        account=934975265,  # 你的机器人的 qq 号
    ),
)


@app.broadcast.receiver("FriendMessage")
async def friend_message_listener(app: Ariadne, friend: Friend):
    await app.send_message(friend, MessageChain([Plain("Hello, World!")]))


@app.broadcast.receiver("GroupMessage", decorators=[DetectPrefix('bot 计算器')])
async def Calculator(app: Ariadne, chain: MessageChain, group: Group):
    if group.id == 322819699 or group.id == 599795569:

        text = str(chain).replace("bot 计算器", "").strip()
        can = "1234567890+-*/()|&^."
        canfun = ["sum"]
        indexOffest = 0
        for i in range(len(text)):
            i += indexOffest
            _break = False
            if (text[i] in can):

                pass
            else:  # 放弃兼容sum
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

            await app.send_group_message(group, MessageChain([str(num)]))
            return
        await app.send_group_message(group, MessageChain("有问题"))


@app.broadcast.receiver("GroupMessage", decorators=[DetectPrefix('bot ')])
async def main(app: Ariadne, chain: MessageChain, group: Group, user: Member):
    if group.id == 322819699 or group.id == 599795569:
        text = str(chain[1])  # 输入处理
        text = text.replace("bot ", "")
        print(text)
        await input_(app, chain, user, group, text)


@app.broadcast.receiver("GroupMessage", decorators=[MentionMe()])  # 注意要实例化
async def on_mention_me(app: Ariadne, chain: MessageChain, group: Group, user: Member):
    if group.id == 322819699 or group.id == 599795569:
        print(str(chain[2]).strip())  # 输入处理
        text = str(chain[2]).strip()
        await input_(app, chain, user, group, text)


async def input_(app, chain, user, group, text):
    ##input_

    if text == "贴贴":  # 贴贴
        await app.send_group_message(group, MessageChain([At(user.id), "贴贴"]))
    if text == "Misaka":
        print("image/" + image.get())
        await app.send_group_message(group, MessageChain([At(user.id), Image(path="image/" + image.get())]))
    if text == "?":
        await app.send_group_message(group, MessageChain(["bot 或@bot开头\n"
                                                          "随机御坂照片: Misaka\n"
                                                          "计算器: 计算器 <算式>(python语法)\n"
                                                          "贴贴: 贴贴\n"]))


app.launch_blocking()
