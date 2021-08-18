# Copyright (C) 2020 
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# Neon UserBot

from userbot import CMD_HELP, ASYNC_POOL, tgbot, SPOTIFY_DC, G_DRIVE_CLIENT_ID, lastfm, LYDIA_API_KEY, YOUTUBE_API_KEY, OPEN_WEATHER_MAP_APPID, AVTO_PP, REM_BG_API_KEY, OCR_SPACE_API_KEY, PM_AUTO_BAN, BOTLOG_CHATID, NEON_VERSION
from userbot.events import register
from telethon import version
from platform import python_version
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("durum")

# ████████████████████████████████ #

def durum(s):
    if s == None:
        return "❌"
    else:
        if s == False:
            return "❌"
        else:
            return "✅"

@register(outgoing=True, pattern="^.durum|^.status")
async def durums(event):

    await event.edit(f"""
**Python {LANG['VERSION']}:** `{python_version()}`
**TeleThon {LANG['VERSION']}:** `{version.__version__}` 
**NEON {LANG['VERSION']}:** `{NEON_VERSION}`

**{LANG['PLUGIN_COUNT']}:** `{len(CMD_HELP)}`

**Inline Bot:** `{durum(tgbot)}`
**Spotify:** `{durum(SPOTIFY_DC)}`
**GDrive:** `{durum(G_DRIVE_CLIENT_ID)}`
**LastFm:** `{durum(lastfm)}`
**YouTube ApiKey:** `{durum(YOUTUBE_API_KEY)}`
**Lydia:** `{durum(LYDIA_API_KEY)}`
**OpenWeather:** `{durum(OPEN_WEATHER_MAP_APPID)}`
**AvtoPP:** `{durum(AVTO_PP)}`
**RemoveBG:** `{durum(REM_BG_API_KEY)}`
**OcrSpace:** `{durum(OCR_SPACE_API_KEY)}`
**Pm AutoBan:** `{durum(PM_AUTO_BAN)}`
**BotLog:** `{durum(BOTLOG_CHATID)}`
**Plugin:** `{LANG['PERMAMENT']}`

**{LANG['OK']} ✅**
    """)
# Esebj / credit : Asena 
# NEON USERBOT


from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
import asyncio


if 1 == 1:
    name = "Profil Fotoğrafları"
    client = "userbot"

@register(outgoing=True, pattern="^.pp(?: |$)(.*)", disable_errors=True)
async def potocmd(event):
    id = "".join(event.raw_text.split(maxsplit=2)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    await event.edit(f"`Gətirilir..`")
    if user:
        photos = await event.client.get_profile_photos(user.sender)
        u = True
    else:
        photos = await event.client.get_profile_photos(chat)
        u = False
    if id.strip() == "":
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
            await event.edit(f"**İstifadəçinin profil şəkilləri uğurla gətirildi! @NeonUserBot**")
        else:
            try:
                if u is True:
                    photo = await event.client.download_profile_photo(user.sender)
                else:
                    photo = await event.client.download_profile_photo(event.input_chat)
                await event.client.send_file(event.chat_id, photo)
                await event.edit(f"İstifadəçinin profil şəkilləri uğurla gətirildi! @NeonUsərBot**")
            except a:
                await event.edit("**Bu istifadəçinin profil şəkili yoxdur.**")
                return
    else:
        try:
            id = int(id)
            if id <= 0:
                await event.edit("**Zəhmət olmasa, birinə cavab verib işlədin modulu.**")
                return
        except:
            await event.edit(f"**Zəhmət olmasa, birinə cavab verib işlədin modulu.**")
            return
        if int(id) <= (len(photos)):
            send_photos = await event.client.download_media(photos[id - 1])
            await event.client.send_file(event.chat_id, send_photos)
        else:
            await event.edit(f"**Söhbətdə Medya Göndərmək Bağlıdır!**")
            await asyncio.sleep(8)
            return


Help = CmdHelp('info')
Help.add_command('durum və ya .status', None, 'Əlavə edilən Apiler və versiyaları göstərər.')
Help.add_command('pp / .pp «rəqəm»','birinə yanıt verərək işlədin.','.pp yanıt - yanıt verdiyiniz insanın bütün profil şekillerini gətirər.\n.pp «hər hansı istifadəçiyə yanıt» «rəqəm» - yazdığınız rəqəm qədər profil şəkilləri gətirər.')
Help.add_info('[N Σ O N](t.me/Neonuserbot) 🇦🇿')
Help.add()
