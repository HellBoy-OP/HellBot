import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, hellversion
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"
PM_IMG = "https://telegra.ph/file/3820fae8e4b4f83a123b1.mp4"
pm_caption = "🔥🔥**卄  卂  尺  尺  丫 YOUR DAD IS ONLINE🔥🔥\n\n\n"

pm_caption += f"⚔️⚔️**MASTER**⚔️⚔️       : {DEFAULTUSER}\n\n"

pm_caption += "🛡️🛡️**TELETHON**🛡️🛡️   : 1.15.0 \n\n"

pm_caption += f"😈😈**Hêllẞø†**😈😈         : `{hellversion}`\n\n"

pm_caption += "⚠️⚠️**CHANNEL**⚠️⚠️     : [ᴊᴏɪɴ](https://t.me/HellBot_Official)\n\n"

pm_caption += "🔱🔱**GROUP**🔱🔱.         : [ᴊᴏɪɴ](https://t.me/HellBot_Official_Chat)\n\n"

pm_caption += "😎😎**LICENSE**😎😎       : [ӀíϲҽղՏҽ](https://github.com/HellBoy-OP/HellBot/blob/master/LICENSE)\n\n"

pm_caption += "🔥🔥**CREATOR🔥🔥      : [HellBot-Owner](https://t.me/kraken_the_badass)\n\n"

pm_caption += " [...▄███▄███▄\n....█████████\n.......▀█████▀\n............▀█▀\n](https://t.me/hellbot_official)\n\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
