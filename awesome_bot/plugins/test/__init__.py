# import nonebot
import urllib.request
import time
from venv import logger

from nonebot import get_driver
from nonebot.adapters.cqhttp import MessageSegment
from nonebot.exception import ActionFailed

from .config import Config

global_config = get_driver().config
config = Config(**global_config.dict())

# Export something for other plugin
# export = nonebot.export()
# export.foo = "bar"

# @export.xxx
# def some_function():
#     pass


from nonebot import on_message, on_command
from nonebot.rule import command, to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event, Message

img_path = "F:/personal/QQRobot/images/"

msg = on_command('', rule=to_me(), priority=1)

error_count = {}

timeout = {}


def download_img(img_url, img_name):
    request = urllib.request.Request(img_url)
    try:
        response = urllib.request.urlopen(request)
        filename = "{}.jpg".format(img_name)
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read())  # 将内容写入图片
            return filename
    except:
        return "failed"


@msg.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    if event.get_plaintext() == "自助表白":
        state['type'] = 'biaobai'
        error_count[event.get_user_id()] = 0
        timeout[event.get_user_id()] = time.time()
        await msg.send(message="表白开始，当你要结束表白时，自行截图聊天记录发送给墙墙，然后再请输入“结束表白”（文字图片不要发在一起），截图只要一张，如果消息太多，请长截图！")
    elif event.get_plaintext() == "自助祝福":
        state['type'] = 'zhufu'
        error_count[event.get_user_id()] = 0
        timeout[event.get_user_id()] = time.time()
        await msg.send(message="祝福开始，当你要结束祝福时，自行截图聊天记录发送给墙墙，然后再请输入“结束祝福”（文字图片不要发在一起），截图只要一张，如果消息太多，请长截图！")
    elif event.get_plaintext() == "自定义信息":
        state['type'] = 'custom'
        error_count[event.get_user_id()] = 0
        timeout[event.get_user_id()] = time.time()
        await msg.send(message="信息记录开始，当你要结束记录时，自行截图聊天记录发送给墙墙，再发送消息类型（如吐槽条，寻人条等），然后再输入“结束记录”（文字图片分开发送），截图只要一张，如果消息太多，请长截图！")
    else:
        await msg.finish("请输入下列选项：\r1.自助表白\r2.自助祝福\r3.自定义信息\r(*￣︶￣)")


@msg.receive()
async def handle_image(bot: Bot, event: Event, state: T_State):
    if time.time() - timeout[event.get_user_id()] > 600:
        await msg.finish("请输入下列选项：\r1.自助表白\r2.自助祝福\r3.自定义信息\r(*￣︶￣)")
    if state['type'] == 'biaobai':
        if event.get_message()[0].type == "image":
            state['image_url'] = event.get_message()[0].data.get('url')
            await msg.reject()
        elif event.get_message()[0].type == "text":
            if event.get_message()[0].data['text'] == "结束表白":
                if state.get("image_url"):
                    state['confirm'] = True
                    message = Message()
                    message.append(MessageSegment.image(state['image_url'])),
                    message.append(MessageSegment.text("输入“确认发送”将发送以上信息到校园墙"))
                    await msg.reject(message)
                else:
                    await msg.finish("未检测到图片，自助表白结束ヾ(￣▽￣)Bye~Bye~")
            if state.get("confirm"):
                if event.get_message()[0].data['text'] == "确认发送":
                    # ret = download_img(state['image_url'], event.get_user_id())
                    await msg.finish('表白成功！(#^.^#)')
                else:
                    error_count[event.get_user_id()] += 1
                    if error_count[event.get_user_id()] > 3:
                        await msg.finish('错误次数过多，表白结束o(╥﹏╥)o')
                    else:
                        await msg.reject('指令有误')
            else:
                await msg.reject()
        else:
            await msg.finish("请说点我能听懂的￣□￣｜｜")
    elif state['type'] == 'zhufu':
        if event.get_message()[0].type == "image":
            state['image_url'] = event.get_message()[0].data.get('url')
            await msg.reject()
        elif event.get_message()[0].type == "text":
            if event.get_message()[0].data['text'] == "结束祝福":
                if state.get("image_url"):
                    state['confirm'] = True
                    message = Message()
                    message.append(MessageSegment.image(state['image_url'])),
                    message.append(MessageSegment.text("输入“确认发送”将发送以上信息到校园墙"))
                    await msg.reject(message)
                else:
                    await msg.finish("未检测到图片，自助祝福结束ヾ(￣▽￣)Bye~Bye~")
            if state.get("confirm"):
                if event.get_message()[0].data['text'] == "确认发送":
                    # ret = download_img(state['image_url'], event.get_user_id())
                    await msg.finish('祝福成功！(#^.^#)')
                else:
                    error_count[event.get_user_id()] += 1
                    if error_count[event.get_user_id()] > 3:
                        await msg.finish('错误次数过多，祝福结束o(╥﹏╥)o')
                    else:
                        await msg.reject('指令有误')
            else:
                await msg.reject()
        else:
            await msg.finish("请说点我能听懂的￣□￣｜｜")
    else:
        if event.get_message()[0].type == "image":
            state['image_url'] = event.get_message()[0].data.get('url')
            await msg.reject()
        elif event.get_message()[0].type == "text":
            if event.get_message()[0].data['text'] == "结束记录":
                if state.get("image_url"):
                    state['confirm'] = True
                    message = Message()
                    message.append(MessageSegment.image(state['image_url'])),
                    message.append(MessageSegment.text(state['msg_type'] + "\r输入“确认发送自定义信息”将发送以上信息到校园墙"))
                    await msg.reject(message)
                else:
                    await msg.finish("未检测到图片，自定义信息结束ヾ(￣▽￣)Bye~Bye~")
            else:
                state["msg_type"] = event.get_message()[0].data['text']
            if state.get("confirm"):
                if event.get_message()[0].data['text'] == "确认发送自定义信息":
                    # ret = download_img(state['image_url'], event.get_user_id())
                    await msg.finish('发布成功！(#^.^#)')
                else:
                    error_count[event.get_user_id()] += 1
                    if error_count[event.get_user_id()] > 3:
                        await msg.finish('错误次数过多，自定义信息结束o(╥﹏╥)o')
                    else:
                        await msg.reject('指令有误')
            else:
                await msg.reject()
        else:
            await msg.finish("请说点我能听懂的￣□￣｜｜")
