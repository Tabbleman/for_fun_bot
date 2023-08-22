from nonebot import on_command, on_keyword, on_regex, on_startswith
from nonebot.rule import to_me, keyword

matcher = on_keyword("算了", rule=to_me(), priority=10, block=True)

@matcher.handle()
async def comfort_people():
  await matcher.send("hi")