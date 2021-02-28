# import nonebot
import urllib.request
import time

from nonebot import get_driver
from nonebot.adapters.cqhttp import MessageSegment

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

biaobai = on_command('自助表白', rule=to_me(), priority=0)

zhufu = on_command('自助祝福', rule=to_me(), priority=0)

custom = on_command('自定义信息', rule=to_me(), priority=0)

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


@biaobai.handle()
async def handle_first_biaobai(bot: Bot, event: Event, state: T_State):
    error_count[event.get_user_id()] = 0
    timeout[event.get_user_id()] = time.time()
    await biaobai.send(message="表白开始，当你要结束表白时，自行截图聊天记录发送给墙墙，然后再请输入“结束表白”（文字图片不要发在一起），截图只要一张，如果消息太多，请长截图！")


@biaobai.receive()
async def handle_biaobai_image(bot: Bot, event: Event, state: T_State):
    if time.time() - timeout[event.get_user_id()] > 600:
        await biaobai.finish("请输入下列选项：\r1.自助表白\r2.自助祝福\r3.自定义信息\r(*￣︶￣)")
    if event.get_message()[0].type == "image":
        state['image_url'] = event.get_message()[0].data.get('url')
        await biaobai.reject()
    elif event.get_message()[0].type == "text":
        if event.get_message()[0].data['text'] == "结束表白":
            if state.get("image_url"):
                state['confirm'] = True
                message = Message()
                message.append(MessageSegment.image(state['image_url'])),
                message.append(MessageSegment.text("输入“确认发送”将发送以上信息到校园墙"))
                await biaobai.reject(message)
            else:
                await biaobai.finish("未检测到图片，自助表白结束ヾ(￣▽￣)Bye~Bye~")
        if state.get("confirm"):
            if event.get_message()[0].data['text'] == "确认发送":
                # ret = download_img(state['image_url'], event.get_user_id())
                await biaobai.finish('测试完成')
            else:
                error_count[event.get_user_id()] += 1
                if error_count[event.get_user_id()] > 3:
                    await biaobai.finish('错误次数过多，表白结束o(╥﹏╥)o')
                else:
                    await biaobai.reject('指令有误')
        else:
            await biaobai.reject()
    else:
        await biaobai.finish("请说点我能听懂的￣□￣｜｜")


@zhufu.handle()
async def handle_first_zhufu(bot: Bot, event: Event, state: T_State):
    error_count[event.get_user_id()] = 0
    timeout[event.get_user_id()] = time.time()
    await zhufu.send(message="祝福开始，当你要结束祝福时，自行截图聊天记录发送给墙墙，然后再请输入“结束祝福”（文字图片不要发在一起），截图只要一张，如果消息太多，请长截图！")


@zhufu.receive()
async def handle_zhufu_image(bot: Bot, event: Event, state: T_State):
    if time.time() - timeout[event.get_user_id()] > 600:
        await zhufu.finish("请输入下列选项：\r1.自助表白\r2.自助祝福\r3.自定义信息\r(*￣︶￣)")
    if event.get_message()[0].type == "image":
        state['image_url'] = event.get_message()[0].data.get('url')
        await zhufu.reject()
    elif event.get_message()[0].type == "text":
        if event.get_message()[0].data['text'] == "结束祝福":
            if state.get("image_url"):
                state['confirm'] = True
                message = Message()
                message.append(MessageSegment.image(state['image_url'])),
                message.append(MessageSegment.text("输入“确认发送”将发送以上信息到校园墙"))
                await zhufu.reject(message)
            else:
                await zhufu.finish("未检测到图片，自助祝福结束ヾ(￣▽￣)Bye~Bye~")
        if state.get("confirm"):
            if event.get_message()[0].data['text'] == "确认发送":
                # ret = download_img(state['image_url'], event.get_user_id())
                await zhufu.finish('测试完成')
            else:
                error_count[event.get_user_id()] += 1
                if error_count[event.get_user_id()] > 3:
                    await zhufu.finish('错误次数过多，祝福结束o(╥﹏╥)o')
                else:
                    await zhufu.reject('指令有误')
        else:
            await zhufu.reject()
    else:
        await zhufu.finish("请说点我能听懂的￣□￣｜｜")


@custom.handle()
async def handle_first_custom(bot: Bot, event: Event, state: T_State):
    error_count[event.get_user_id()] = 0
    timeout[event.get_user_id()] = time.time()
    await custom.send(message="信息记录开始，当你要结束记录时，自行截图聊天记录发送给墙墙，在最后一条消息发送消息类型（如吐槽条，寻人条，感慨条等），然后再请输入“结束记录”（文字图片不要发在一起），截图只要一张，如果消息太多，请长截图！")
    # await custom.send(message="测试测试")


@custom.receive()
async def handle_custom_image(bot: Bot, event: Event, state: T_State):
    if time.time() - timeout[event.get_user_id()] > 600:
        await custom.finish("请输入下列选项：\r1.自助表白\r2.自助祝福\r3.自定义信息\r(*￣︶￣)")
    if event.get_message()[0].type == "image":
        state['image_url'] = event.get_message()[0].data.get('url')
        await custom.reject()
    elif event.get_message()[0].type == "text":
        if event.get_message()[0].data['text'] == "结束记录":
            if state.get("image_url"):
                state['confirm'] = True
                message = Message()
                message.append(MessageSegment.image(state['image_url'])),
                message.append(MessageSegment.text(state['custom_type'] + "\r输入“确认发送自定义信息”将发送以上信息到校园墙"))
                await custom.reject(message)
            else:
                await custom.finish("未检测到图片，自定义信息结束ヾ(￣▽￣)Bye~Bye~")
        else:
            state["custom_type"] = event.get_message()[0].data['text']
        if state.get("confirm"):
            if event.get_message()[0].data['text'] == "确认发送自定义信息":
                # ret = download_img(state['image_url'], event.get_user_id())
                await custom.finish('测试完成')
            else:
                error_count[event.get_user_id()] += 1
                if error_count[event.get_user_id()] > 3:
                    await custom.finish('错误次数过多，自定义信息结束o(╥﹏╥)o')
                else:
                    await custom.reject('指令有误')
        else:
            await custom.reject()
    else:
        await custom.finish("请说点我能听懂的￣□￣｜｜")


@msg.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    await msg.finish("请输入下列选项：\r1.自助表白\r2.自助祝福\r3.自定义信息\r(*￣︶￣)")
