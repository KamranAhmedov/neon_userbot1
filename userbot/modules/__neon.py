# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Neon UserBot

from userbot.cmdhelp import CmdHelp
from userbot import cmdhelp
from userbot import NEON_STIK, OWNERS, NEON_VERSION
from userbot import CMD_HELP
from userbot.events import register

from userbot.language import get_value
LANG = get_value("__neon")


@register(outgoing=True, pattern="^.neon(?: |$)(.*)")
async def neon(event):
    """ necesen """
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(LANG["NEED_PLUGIN"])
    else:
        string = ""
        sayfa = [sorted(list(CMD_HELP))[i:i + 5] for i in range(0, len(sorted(list(CMD_HELP))), 5)]
        
        for i in sayfa:
            string += f'{NEON_STIK} '
            for sira, a in enumerate(i):
                string += "__" + str(a)
                if sira == i.index(i[-1]):
                    string += "__"
                else:
                    string += "__, "
            string += "\n"
        await event.edit(LANG["NEED_MODULE"] + '\n\n' + string)

        
@register(incoming=True, from_users=OWNERS, pattern="^.live$")
async def ownerlive(owner):
    if owner.fwd_from:
        return
    if owner.is_reply:
        reply = await owner.get_reply_message()
        replytext = reply.text
        reply_user = await owner.client.get_entity(reply.from_id)
        ren = reply_user.id
        if owner.sender_id == 1929222125:
            neon = "Ətağa"
        else:
            neon = "Ətağa"
        if ren == 1929222125:
            Version = str(NEON_VERSION.replace("v","")) 
            await owner.reply(f"**{neon}** **N Σ O N aktivdir...🈴**\n**N Σ O N Version:** `{NEON_VERSION}` 🔫")
        else:
            return
    else:
        return 
               
