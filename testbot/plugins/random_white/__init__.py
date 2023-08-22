from nonebot.adapters.onebot.v11 import *
from nonebot.rule import to_me, is_type
from nonebot import on_command, on_keyword
from nonebot.adapters.onebot.v11 import *
import os, random
white_silk = on_command("随机白丝", rule=is_type(GroupMessageEvent), aliases={'sese', 'setu'}, priority=10, block=True)

FILE_HEADER = "file://"
ROOT_DIR = "/home/z/projects/tmp/testbotV0-0/test/white"
WHITES = []
for root, dirs, files in os.walk(ROOT_DIR):
    for file in files:
        WHITES.append(os.path.join(root, file))

@white_silk.handle()
async def handle_function() :
  black = random.choice(WHITES)
  message = MessageSegment.image(file=f"{FILE_HEADER}{black}")
  await white_silk.send(message)
  

