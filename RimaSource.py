########## [ IMPORTING LIBRARIES ] ##########
import os
import time
import random

########## [ LAUNCH SCREEN ] ##########
titles = ["Скочад дедкорд", "Многа мяса, мала теста!", "dsc.gg/mamcom", "бебракор в4", "Продам гараж", "взламаеш челавека?", "Маенкравт моя жизнн", "5 раток 3 майнера", "Противотанковая установка САУ B2", "дима тушенка💔", "захадите на сервер 127.0.0.1", "Я поддерживаю чёрно-белый лгбт", "крео-паста"]
os.system("title RIMASELF / -_ Version: 1.0 -_")
os.system("color d")
os.system("cls")
print(f'''
               ____   ____ __  ___ ___    _____  ______ __     ______
              / __ \ /  _//  |/  //   |  / ___/ / ____// /    / ____/   
             / /_/ / / / / /|_/ // /| |  \__ \ / __/  / /    / /_       Created with love <3
            / _, _/_/ / / /  / // ___ | ___/ // /___ / /___ / __/       Developed by TurboKoT
           /_/ |_|/___//_/  /_//_/  |_|/____//_____//_____//_/       
                                                                     
                                    {random.choice(titles)}                             ''')

time.sleep(5)
os.system("cls")
########## [ CHECKING TOKEN ] ##########
if not os.path.isfile("rimatoken.txt"):
    print("[ERROR] Не удалось найти файл токена.\nНо, скорее всего это означает что вы - новый пользователь!\nСейчас я создам файл в текущей директории, и открою его.\nВместо того что там написанно, введите ваш токен.\n\nПосле этого нажмите Enter!")
    file = open('rimatoken.txt', 'w')
    file.write("Привет! Введи вместо этого текста токен;)")
    file.close()
    os.system("start rimatoken.txt")
    input()
    os.system("cls")

########## [ IMPORTING LIBRARIES ] ##########
from asyncio import sleep
import discord
from discord.ext import commands

########## [ VARIABLES ] ##########
bull1 = ["еблан, ", "у твоей матери ребенок", "насколько же ты", "ты униженный и попущеный", "слышь ты блядь, уебан.", "слитое уродское создание", "cын еблана отзовись.", "ау блядь уебище.", "блядское создание ", "ущербный настолько что твое призвание", "мамонт ебаный", "проведи себе вскрытие нахуй, ты", "ты смешной, долбоящер", "Что ты несешь долбаебище ", "Ау блядь, ", "Дочка прошмандовки, "]
bull2 = [" шлюха,", " хуисосище ебанное", " пидорасня", " животное", " мальчик без хуя", " спидозная залупа", " ущербное создание", " хуежуйка ебаная", " отмороженный ", " подзалупный творожочек", " долбаебическая свинья", " сын шлюхи", " ребенок двух пидорасов", " терпилоид чисто", " сын детственника", " сын овцы", " дилдосос", " порноактер из категории гей порно", " обсос", " подсос своего бати", " жертва аутизма", " абортышь", "  даун чисто", " недоразвитое создание", " ебучая ошибка природы", " дитя ебаное", " долбаеб", " оффни свой ебасос", " подсос всех кто мужского пола ебать", " чисто уебище ебаное блядь", " дырявый отморозок", " у тебя четыре хуя в жопе, хватит", " самоунижается чисто", "чисто ребенок гноя блядь", " какого хуи сосать уеба", " гнойная хуйня", " ущербный подсос ебать ахахаа", " порвало тебя да,"]
bull3 = [" гандопляс ебаный", " сын джастнаникса и дочь итскекофа ", " безмамное чудище", " слитое уродское создание", " переебанный отцами", " бомж", ", позови мать проститутку уебище", " про тебя принято называть животным, потому-что ты отсталый долбаеб нахуй,", " хуйло ебанное", " у тебя очко растянуто настолько, что туда влезает ебанный вентилятор нахуй", " шалашовка пиздочесанная", " ебучий хуебес", ",  разьебали бедного нахуй.", " уркодроченый пидорас озабоченых пенсионеров блядь. ", " блядота", " клиторосос ебучий",  " пидораст конченый", " сын залупы", " чисто мальчик гей нахуй", " выебистый пёс", " иди матери поплачь", " спермаглот ебаный", " подсос больших хуев", " иди матери пожалуйся чтоле", " сын куколда и проститутки", " у тебя в очке уже вазелиновые железы образовались, уебище,",  " ты при виде плетки сразу раком встаешь", " хватит высирать свою хуйню,", " дитя чернобыля", " хватит пастить уебок", " хватит выебываться, раб, без еды останешься, гандон"]
bull4 = [". Вообще нахуя ты так с отцом разговариваешь", ', че замолк сын чудовища', ". Я бы тебя отпиздил, хуесос", ", че молчим", ", давай, метни стрелочку, лучница ебаная", " попизди на меня еще, хуесоска :)", " :heart:", " сразу рот прирыл", " с хуями во рту говорить не можешь? Псина", ", что молчишь, жертва двух озабоченых подростков и бутылки водки", ". И вообще ты жертва аборта", ". Давай, голос, пёс.", ". Че блядь, погавкал и все?", "мы тебя по кругу пускали, чорт", ", я тебя палкой хуярил", ", мать твоя видя мой огромный член течет, уебище", ". Твоя мать под моим столом кстати", ". Я тебя елдаком по голове уебашил", ". Ты - одноклеточное существо.", ". Кринжовый хуеплет", ". Запомни нахуй, я - твой хозяин, а ты секс-рабыня", " хули ты мне сосать перестал, я не разрешал нахуй", ", кстати я тебе команду голос не давал, хули пиздишь уеба", ". Я слышал твоя мать элитная шлюха, попроси ее заскочить ко мне, давно не ебались"]
ball_answers = ["Возможно", "Да", "Нет", "Не знаю"]
active = False

client = commands.Bot(command_prefix = ".", self_bot = True)
client.remove_command('help')

@client.event
async def on_ready():
    print("[INFO] * RIMASELF SUCESSFULLY LOADED!")

@client.event
async def on_command_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.CommandNotFound):
        z = await ctx.send('''```ansi
[2;31mКоманда не найдена.[0m Напишите [2;34m.help[0m для просмотра доступных команд[2;41m[0m
```''')
        await sleep(5)
        await z.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
        z = await ctx.send('''```ansi
[2;31mВы [1;31mне[0m[2;31m ввели нужные [2;35mаргументы[0m[2;31m в данной команде![0m[2;41m[0m
```''')
        await sleep(5)
        await z.delete()
    else: print(f"[ERROR] * {error}")

@client.command()
async def help(ctx):
    await ctx.channel.purge(limit=1)
    z = await ctx.send('''```ansi
┌💟┐  [1;2m[1;35mＲＩＭＡＳＥＬＦ[0m[0m
└💫┘   Prefix: .

「😎」 [2;33m[1;33mF U N[0m[2;33m[0m
  [  -  ]  [2;33mspam[0m <кол-во> <текст/null/moblag/pclag> [2;35m| Начать спам[0m
  [  -  ]  [2;33mball[0m <вопрос> [2;35m| Спросить шар[0m
  [  -  ]  [2;33membed[0m <название> <цвет (hex)> <описание> [2;35m| Отправить embed[0m
  [  -  ]  [2;33mpopit[0m [2;35m| Поп-ит[0m

「☄️」 [1;2m[1;34mO T H E R[0m[0m
  [  -  ]  [2;34mping[0m [2;35m| Пинг
[0m  [  -  ]  [2;34mactivity[0m <playing/streaming/watching> <текст> [2;35m| Изменить статус[0m

「🤬」 [2;31m[1;31mB U L L I N G[0m[2;31m[0m
  [  -  ]  [2;31mbullstart[0m [2;35m| Включить буллинг[0m
  [  -  ]  [2;31mbullstop[0m [2;35m| Выключить буллинг[0m
[2;32m[0m
```''')
    await sleep(7)
    await z.delete()

########## [ FUN ] ##########

@client.command()
async def spam(ctx, kv, *, text):
    await ctx.channel.purge(limit=1)
    if text == "null":
        while int(kv) !=0:
            await ctx.send("||\n||")
            kv = int(kv)-1
    elif text == "moblag":
        while int(kv) !=0:
            await ctx.send("⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟")
            kv = int(kv)-1
    elif text == "pclag":
        while int(kv) !=0:
            await ctx.send(":chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains::chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains::chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains::chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains::chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains::chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains::chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains::chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains:")
            kv = int(kv)-1
    else:
        while int(kv) !=0:
            await ctx.send(text)
            kv = int(kv)-1

@client.command()
async def ball(ctx):
    await ctx.channel.purge(limit=1)
    z = await ctx.send(f'''```ansi
└🔮┘

Вы потрясли [2;34mмагический шар[0m, на нем написанно: [2;35m[1;35m{random.choice(ball_answers)}[0m[2;35m[0m[2;41m[0m
```''')
    await sleep(5)
    await z.delete()

@client.command()
async def embed(ctx, title, color="ffffff", *, description=""):
    await ctx.channel.purge(limit=1)
    print("[INFO] * Embed Sent!")
    await ctx.send(f"https://embed.rauf.wtf/?author=&title={title}&description={description}&color={color}&image=&redirect=".replace(" ", "+"))

@client.command()
async def popit(ctx):
    await ctx.channel.purge(limit=1)
    print("[INFO] * Pop-It Sent!")
    await ctx.send("||⬜||||⬜||||⬜||||⬜||||⬜||\n||🟩||||🟩||||🟩||||🟩||||🟩||\n||🟨||||🟨||||🟨||||🟨||||🟨||\n||🟦||||🟦||||🟦||||🟦||||🟦||\n||🟧||||🟧||||🟧||||🟧||||🟧||")

########## [ OTHER ] ##########

@client.command()
async def ping(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send("Понг " + str(round(client.latency)) + "мс")

@client.command()
async def activity(ctx, stype, *, text):
    await ctx.channel.purge(limit=1)
    if stype == "playing":
        await client.change_presence(activity = discord.Game(text))
        print("[INFO] * Activity has been changed!")
        z = await ctx.send('''```ansi
└🎮┘

[2;32mАктивность [2;32m[1;32mуспешно[0m[2;32m[0m[2;32m изменена![0m

[2;32m[0m
```''')
        await sleep(5)
        await z.delete()
    elif stype == "streaming":
        await client.change_presence(activity = discord.Streaming(name=text, url="https://www.twitch.tv/directory/game/Minecraft?lang=ru%22"))
        print("[INFO] * Activity has been changed!")
        z = await ctx.send('''```ansi
└💥┘

[2;32mАктивность [2;32m[1;32mуспешно[0m[2;32m[0m[2;32m изменена![0m

[2;32m[0m
```''')
        await sleep(5)
        await z.delete()
    elif stype == "watching":
        await client.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name=text))
        print("[INFO] * Activity has been changed!")
        z = await ctx.send('''```ansi
└👀┘

[2;32mАктивность [2;32m[1;32mуспешно[0m[2;32m[0m[2;32m изменена![0m

[2;32m[0m
```''')
        await sleep(5)
        await z.delete()
    else:
        z = await ctx.send('''```ansi
[2;31mВы [1;31mнеправильно[0m[2;31m указали тип активности![0m[2;32m[0m
```''')
        await sleep(5)
        await z.delete()

########## [ BULLING ] ##########

@client.command()
async def bullstart(ctx):
    await ctx.channel.purge(limit=1)
    global active

    active = True
    bulls = 0

    while active:
        await sleep(random.randint(1, 2))
        async with ctx.typing():
            await sleep(random.randint(2, 4))
            await ctx.send(random.choice(bull1) + random.choice(bull2) + random.choice(bull3) + random.choice(bull3) + random.choice(bull4))
            bulls = bulls+1
            print("[INFO] * Bulling sent! Total:", bulls)

@client.command()
async def bullstop(ctx):
    await ctx.channel.purge(limit=1)
    global active
    active = False
    print("[INFO] * Bulling stopped!")
    await sleep(1)
    global oskov
    oskov = 0

try:
    client.run(open( 'rimatoken.txt', 'r' ).readline(), bot = False)
except:
    print("[ERROR] Вы ввели неккоректный токен!\n\nНажмите Enter для выхода..")
    input()
