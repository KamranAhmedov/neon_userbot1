import asyncio
from telethon import events
from userbot import SUDO_ID, SUDO_VERSION, NEON_VERSION
from userbot.cmdhelp import CmdHelp
from userbot.events import register

@register(incoming=True, from_users=SUDO_ID, pattern="^.slive$")
async def _(e):
    await e.client.send_message(e.chat_id,f"**N Σ O N**\n**Sudo aktivdir...** ✅\n**N Σ O N Version:** `{NEON_VERSION}`\n**Sudo Version:** `{SUDO_VERSION}`")
    
Help = CmdHelp('sudo').add_command(
        'slive',None,'Sudo aktiv olub olmadığını yoxlamaq üçün.'
    ).add_command(
        'spromote', '<istifadəçi adı/cavəblama> <xüsusi ad (istəyə bağlı)>', 'Seçdiyiniz istifadəçiyə qrupu idarə icazəsi verir.'
    ).add_command(
        'sdemote', '<istifadəçi adı/cavablama>', 'Seçdiyiniz userin idarəçilik icazəsini alar.'
    ).add_command(
        'sban', '<istifadəçi adı/cavablama> <səbəb (istəyə bağlı)>', 'Seçdiyiniz istifadəçinin mesaj yazmasını dayandırar, idarəçilərdədə də işləyir.'
    ).add_command(
        'sunban', '<istifadəçi adı/cavablama>', 'Verilən qadağanı(ban) qaldırır.'
    ).add_command(
        'skick', '<istifadəçi adı/cavablama> <səbəbi (istəyə bağlı)>', 'Qrupdan göstərdiyiniz istifadəçini çıxardar.'
    ).add_command(
        'sgmute', '<istifadəçi adı/cavablama> <səbəbi (istəyə bağlı)>', 'İstifadəçi idarə etdiyiniz bütün qruplarda səssizə alınır.'
    ).add_command(
        'sungmute', '<istifadəçi adı/cavablama>', 'İstifadəçini qlobal olaraq səssizə alınanlar siyahısından silər.'
    ).add_command(
        'sqruptemizle', None, 'Bir qrupdakı silinmiş hesabları axtarır. Qrupdakı silinən hesabları çıxarmaq üçün .qruptemizle sil əmrini istifadə edin.'
    ).add_command(
        'admin', None, 'Söhbət idarəçilərinin siyahısını alır.'
    ).add_command(
        'sbots', None, 'Qrupda olan botları göstərir.'
    ).add_command(
        'sqrup', '<istifadəçi adı> <istifadəçi adı/cavablama>', 'Söhbətdəki bütün (və ya axtarılan) istifadəçiləri siyahıya alır.'
    ).add_command(
        'setgppic', '<cavablanan şəkil>', 'Qrupun şəklini dəyişdirir.'
    ).add_command(
        'swarn', '<istifadəçi adı/cavablama> <sebep (isteğe bağlı>', 'Belirttiğiniz kullanıcıyı uyarır.'
    ).add_command(
        'sunwarn', '<istifadəçi adı/cavablama> <sebep (isteğe bağlı>', 'Belirttiğiniz kullanıcının uyarısını kaldırır.'
    ).add_command(
        'warn', '<istifadəçi adı/cavablama> <səbəb (istəyə bağlı>', 'Göstərdiyiniz istifadəçiyə xəbərdarlıq edər.'
    ).add_command(
        'sneonsil', None, 'Qrupda silinmiş hesabları göstərir.'
    ).add_command(
        'add', '<istifadəço ad(lar)ı>', 'qrupa istədiyiniz hesabı əlavə edər.'
    ).add_command(
        'sgban', '<istifadəçi adı/cavablama>', 'İstifadəçini qlobal olaraq qadağan edin.'
    ).add_command(
        'sungban', '<istifadəçi adı/cavablama>', 'İstifadəçinin qlobal qadağasını qaldırır.'
    ).add_command(
        'spin', '<cavablama>', 'Cavab verdiyiniz mesajı sabitləyər.'
    ).add_command(
        'setgpic', '<cavablama>', 'Qrup fotosunu dəyişdirir.'
    ).add()

