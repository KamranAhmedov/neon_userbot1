from userbot import bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from telethon import events

@register(outgoing=True, disable_errors=True, pattern=r"^\.open(?: |$)(.*)")
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    a = await event.reply("**Fayl oxunur...**")
    if len(c) > 4095:
        await a.edit("`Bağışlayın, bir xəta baş verdi.`")
    else:
        await event.client.send_message(event.chat_id, f"```{c}```")
        await a.delete()
    os.remove(b)
  
Help = CmdHelp('doc')
Help.add_command('open', '<bir fayla cavab>', 'Faylın məzmununu oxuyun və Telegram mesajı olaraq göndərin.')
Help.add()
