from nonebot.adapters.onebot.v11 import *
from nonebot.rule import to_me
from nonebot import on_command
from nonebot.adapters.onebot.v11 import *
__plugin_name__ = 'ping'
__plugin_usage__ = 'usage: say /weather'
weather = on_command("weather", rule=to_me(), aliases={"weather", "查天气"}, priority=10, block=True)

@weather.handle()
async def handle_function() :
  message = MessageSegment.image(file="file:///home/z/projects/tmp/testbotV0-0/test/black/141.jpg")
  await weather.send(message)
  

