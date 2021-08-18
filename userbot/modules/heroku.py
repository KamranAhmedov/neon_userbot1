# Neon UserBot / t.me/NeonUserBot

import codecs
import heroku3
import asyncio
import aiohttp
import math
import os
import ssl
import requests

from userbot import (
    HEROKU_APPNAME,
    HEROKU_APIKEY,
    BOTLOG,
    BOTLOG_CHATID
)

from userbot.events import register
from userbot.cmdhelp import CmdHelp

heroku_api = "https://api.heroku.com"
if HEROKU_APPNAME is not None and HEROKU_APIKEY is not None:
    Heroku = heroku3.from_key(HEROKU_APIKEY)
    app = Heroku.app(HEROKU_APPNAME)
    heroku_var = app.config()
else:
    app = None


@register(outgoing=True, pattern=r"^.(get|del) var(?: |$)(\w*)")
async def variable(var):
    exe = var.pattern_match.group(1)
    if app is None:
        await var.edit("`[HEROKU]"
                       "\n**HEROKU_APPNAME** yoxdur. @NeonSUP dəstək qrupuna gəlib dəstək alaraq quraşdırın.")
        return False
    if exe == "get":
        await var.edit("`Heroku Məlumatlarə gətiririlir...`")
        variable = var.pattern_match.group(2)
        if variable != '':
            if variable in heroku_var:
                if BOTLOG:
                    await var.client.send_message(
                        BOTLOG_CHATID, "#CONFIGVAR\n\n"
                        "**ConfigVar**:\n"
                        f"`{variable}` = `{heroku_var[variable]}`\n"
                    )
                    await var.edit("**BOTLOG qrupuna göndərildi...**")
                    return True
                else:
                    await var.edit("`Zəhmət olmasa BOTLOG'u True olaraq təyin edin...`\n`Əgər başa düşmədinizsə` @NeonSUP `dəstək qrupumuza gəlin.`")
                    return False
            else:
                await var.edit("`Məlumatlar yoxdu...`")
                return True
        else:
            configvars = heroku_var.to_dict()
            if BOTLOG:
                msg = ''
                for item in configvars:
                    msg += f"`{item}` = `{configvars[item]}`\n"
                await var.client.send_message(
                    BOTLOG_CHATID, "#CONFIGVARS\n\n"
                    "**ConfigVars**:\n"
                    f"{msg}"
                )
                await var.edit("`BOTLOG_CHATID alındı...`")
                return True
            else:
                await var.edit("`Zəhmət olmasa BOTLOG'u True olaraq təyin edin...`\n`Əgər başa düşmədinizsə` @NeonSUP `dəstək qrupumuza gəlin.`")
                return False
    elif exe == "del":
        await var.edit("`Məlumatlar silinir...`")
        variable = var.pattern_match.group(2)
        if variable == '':
            await var.edit("`Silmək istədiyiniz ConfigVars'ı seçin.`")
            return False
        if variable in heroku_var:
            if BOTLOG:
                await var.client.send_message(
                    BOTLOG_CHATID, "#DELETECONFIGVAR\n\n"
                    "**ConfigVAR Silindi**:\n"
                    f"`{variable}`"
                )
            await var.edit("`Heroku Məlumatlar Silindi...`")
            del heroku_var[variable]
        else:
            await var.edit("`Belə Məlumat Yoxdu...`")
            return True


@register(outgoing=True, pattern=r'^.set var (\w*) ([\s\S]*)')
async def set_var(var):
    await var.edit("`Məlumatlar Hazırlanır...`")
    variable = var.pattern_match.group(1)
    value = var.pattern_match.group(2)
    if variable in heroku_var:
        if BOTLOG:
            await var.client.send_message(
                BOTLOG_CHATID, "#SETCONFIGVAR\n\n"
                "**Yeni CofigVAR Dəyişikliyi**:\n"
                f"`{variable}` = `{value}`"
            )
        await var.edit("`Məlumatlarınız Herokuya Yazılır...`")
    else:
        if BOTLOG:
            await var.client.send_message(
                BOTLOG_CHATID, "#CONFİGVAR\n\n"
                "**Yeni ConfigVAR**:\n"
                f"`{variable}` = `{value}`"
            )
        await var.edit("`Məlumatlarınız Əlavə Edildi...`")
    heroku_var[variable] = value



@register(outgoing=True, pattern=r"^\.loq")
async def _(dyno):
    try:
        Heroku = heroku3.from_key(HEROKU_APIKEY)
        app = Heroku.app(HEROKU_APPNAME)
    except BaseException:
        return await dyno.reply(
            "`Zəhmət olmasa,Heroku VARS'da Heroku API Key və Heroku APP name'in düzgün olduğundan əmin olun.`"
        )
    await dyno.edit("`Loq gətirilir....`")
    with open("logs.txt", "w") as log:
        log.write(app.get_log())
    fd = codecs.open("logs.txt", "r", encoding="utf-8")
    data = fd.read()
    key = (requests.post("https://nekobin.com/api/documents",
                         json={"content": data}) .json() .get("result") .get("key"))
    url = f"https://nekobin.com/raw/{key}"
    await dyno.edit(f"`Heroku loq'u :`\n\n: [N Σ O N]({url})")
    return os.remove("logs.txt")


CmdHelp('heroku').add_command(
                            'set var',
                            'Bunun sayəsində mövcüd heroku VAR-larınızı dəyişə bilərsiniz.\nVə yaxud da yeni varlar əlavə edə bilərsiniz.'
                            ".set var NEON_STIK 🈴"
).add_command(
    'get var', None, 'VAR-larınıza baxın. Lakin, özəl BOTLOG qrupunuzda istifadə edin.'
).add_command(
    'del var', None,'Mövcüd Heroku Varlarınızı bu əmr sayəsində silə bilərsiniz.'
).add_command(
    'loq', None, 'Heroku loqu'
).add()
