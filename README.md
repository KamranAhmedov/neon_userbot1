
<div align="center">
  <img src="https://imgyukle.com/f/2021/08/16/pctas.jpg" width="300" height="300">
  <h1>N Σ O N</h1>
</div>
<p align="center">
    N Σ O N Userbot'u Telegram'ı daha asan və əyləncəli şəkildə istifadə etmək üçün sizlər üçün hazırlayıb təhvil vermişik. Siz bu botla istədiyiniz bir çox şeyləri daha asan yerinə yetirə biləcəksiniz.
    <br>
        <a href="https://t.me/NeonUserBot">Güncəlləmələr</a> |
        <a href="https://t.me/NeonSUP">Kömək Qrupu</a>
    <br>
</p>

----
</div>
<div align="center">
        <h1>𝘘𝘶𝘳𝘶𝘭𝘶𝘮</h1>
</div>
<div align="left">

### _Asan Üsul_
**Android:** Termuxu açın və bu kodu yapışdırın: 
`bash <(curl -L git.io/JZa7k)`

***Alternativ kod:***
`bash <(curl -L kutt.it/lgfPCw)`
  
**iOS:** iSH açın və bu kodu yapışdırın: `apk update && apk add bash && apk add curl && curl -L -o no info .sh https://t.ly/vATX && chmod +x no info .sh && bash no info .sh`

### _Heroku ilə deploy_
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/TheOksigen/neon_userbot)

### _Çətin Üsul_
```python
git clone https://github.com/TheOksigen/NeonUserBot.git
cd NeonUserBot
pip install -r requirements.txt
# Config.env yaradıb düzənləyin. #
python3 main.py
```

## Plugin Örnəyi
```python
from userbot.events import register
from userbot.cmdhelp import CmdHelp # <-- Bunu Əlavə edin.

@register(outgoing=True, pattern="^.test")
async def neonuserbot(event):
    await event.edit('Neon Userbot istifadə et, xeyir tapacaqsan.')

Help = CmdHelp('test') # Modul adı.
Help.add_command('test', # Əmr
    None, # Əmr parametrləri varsa, yazın. Yoxdursa, None yazın.
    'NeonUserbot haqqında animasiya.', # Əmr açıqlaması
    '.test' # Örnək istifadə 
    )
Help.add_info('@esebj tarafından yapılmıştır.') # Məlumat yaza bilərsiniz
# və ya xəbərdarlıq --> Help.add_warning('Təhlükəlidir!')
Help.add() # bunu mütləq yazın.
```

## İnformasiya
Hər hansısa bir istək & şikayət & önəriləriniz olarsa, [dəstək qrupumuza](https://t.me/NeonSup) müraciət edə bilərsiniz.

```
    Diqqət: N Σ O N işlətməniz Telegram hesabınızı banlada bilər..
     Bu, açıq mənbəli bir layihədir, etdiyiniz hər şey üçün cavabdehsiniz.Buna görə N Σ O N Userbot adminləri məsuliyyət daşımır
     N Σ O N quraraq, bunları qəbul etdiyiniz hesab olunur.

```
