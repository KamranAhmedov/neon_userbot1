import asyncio
from telethon import events
from userbot import SUDO_ID, SUDO_VERSION, NEON_VERSION
from userbot.cmdhelp import CmdHelp
from userbot.events import register

@register(incoming=True, from_users=SUDO_ID, pattern="^.slive$")
async def _(e):
    await e.client.send_message(e.chat_id,f"**N Σ O N**\n**Sudo aktivdir...** ✅\n**N Σ O N Version:** `{NEON_VERSION}`\n**Sudo Version:** `{SUDO_VERSION}`")
    
Help = CmdHelp('sudo')
Help.add_command('slive',None,'Sudo aktiv olub olmadığını yoxlamaq üçün.')
Help.add()

