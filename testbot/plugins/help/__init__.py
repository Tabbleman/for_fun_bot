from nonebot import on_command
from nonebot.rule import is_type, to_me 
from nonebot.adapters.onebot.v11 import Message, MessageSegment,GroupMessageEvent

help = on_command("help", rule=to_me(), aliases={"help", "小助手"}, priority=10, block=True)

@help.handle()
async def get_help():
  await help.send("TODO", priority=10, block=True)