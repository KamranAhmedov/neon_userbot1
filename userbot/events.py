# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# N Σ O N 

""" Hadiseleri idare etmek üçün User Bot modulu.
 UserBot'un esas komponentlerinden biri. """

import sys
from asyncio import create_subprocess_shell as asyncsubshell
from asyncio import subprocess as asyncsub
from os import remove
from time import gmtime, strftime
from traceback import format_exc

from telethon import events

from userbot import bot, BOTLOG_CHATID, LOGSPAMMER, PATTERNS


def register(**args):
    """ Yeni bir feailiyyet qeyd edin """
    pattern = args.get('pattern', None)
    disable_edited = args.get('disable_edited', False)
    groups_only = args.get('groups_only', False)
    trigger_on_fwd = args.get('trigger_on_fwd', False)
    trigger_on_inline = args.get('trigger_on_inline', False)
    disable_errors = args.get('disable_errors', False)

    if pattern:
        args["pattern"] = pattern.replace("^.", "^["+ PATTERNS + "]")
    if "disable_edited" in args:
        del args['disable_edited']

    if "ignore_unsafe" in args:
        del args['ignore_unsafe']

    if "groups_only" in args:
        del args['groups_only']

    if "disable_errors" in args:
        del args['disable_errors']

    if "trigger_on_fwd" in args:
        del args['trigger_on_fwd']
      
    if "trigger_on_inline" in args:
        del args['trigger_on_inline']

    def decorator(func):
        async def wrapper(check):
            if not LOGSPAMMER:
                send_to = check.chat_id
            else:
                send_to = BOTLOG_CHATID

            if not trigger_on_fwd and check.fwd_from:
                return

            if check.via_bot_id and not trigger_on_inline:
                return
             
            if groups_only and not check.is_group:
                await check.respond("**Bu modul qrup üçün nəzərdə tutulub.**\n**Lakin, mən buranın qrup olduğuna inanmıram** 🤔")  
                return

            try:
                await func(check)
                

            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except BaseException:
                if not disable_errors:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    text = "**USER BOT XETA HESABATI**\n"
                    link = "[N Σ O N](https://t.me/NeonSup)"
                    text += "İstəsəniz bunu şikayət edə bilərsiniz"
                    text += f" - sadəcə bu mesajı buraya göndərin {link}.\n"
                    text += "Xəta və Tarixdən başqa heçnə qeyd edilmir\n"

                    ftext = "========== XƏBƏRDARLIQ =========="
                    ftext += "\nBu faylı sadece bura yüklendi,"
                    ftext += "\nsadece xeta ve tarix hissesini qeyd etdik,"
                    ftext += "\nşexsi melumatlarınıza hörmet edirik,"
                    ftext += "\nburada hansısa şexsi melumatınız varsa"
                    ftext += "\nbu xeta hesabatı olmaya biler, kimse melumatlarınıza baxa bilmez.\n"
                    ftext += "================================\n\n"
                    ftext += "--------N Σ O N⚡️𝐔𝐬𝐞𝐫𝐁𝐨𝐭🇦🇿 XETA HESABATI--------\n"
                    ftext += "\nTarix: " + date
                    ftext += "\nQrup ID: " + str(check.chat_id)
                    ftext += "\nGönderen İsdifadeçinin ID: " + str(check.sender_id)
                    ftext += "\n\nHadise:\n"
                    ftext += str(check.text)
                    ftext += "\n\nİzleme Melumatı:\n"
                    ftext += str(format_exc())
                    ftext += "\n\nXeta:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n--------USERBOT XETA HESABATI SONLUQ--------"

                    command = "git log --pretty=format:\"%an: %s\" -10"

                    ftext += "\n\n\nSon 10 commit:\n"

                    process = await asyncsubshell(command,
                                                   stdout=asyncsub.PIPE,
                                                  stderr=asyncsub.PIPE)
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) \
                        + str(stderr.decode().strip())

                    ftext += result

                    file = open("neon.log", "w+")
                    file.write(ftext)
                    file.close()

                    if LOGSPAMMER:
                        await check.client.respond("`Bağışla, [N Σ O N](https://t.me/NeonSup) çökdü.\
                        \nXeta hesabatları UserBot gündelik qrupunda gizlener.`")

                    await check.client.send_file(send_to,
                                                 "neon.log",
                                                 caption=text)
                    remove("neon.log")
            else:
                pass
        if not disable_edited:
            bot.add_event_handler(wrapper, events.MessageEdited(**args))
        bot.add_event_handler(wrapper, events.NewMessage(**args))

        return wrapper

    return decorator
