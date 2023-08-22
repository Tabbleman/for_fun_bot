from nonebot import on_command
from nonebot.rule import to_me, is_type
from nonebot.adapters.onebot.v11 import Message, GroupMessageEvent


heartbeat = on_command(cmd="heartbeat", rule=is_type(GroupMessageEvent) ,aliases={"heartbeats"}, priority=10, block=True)

@heartbeat.handle()
async def handle_heartbeat():
  await heartbeat.send("我的心脏还在跳动啊！")