import telebot
from telebot import types

bot = telebot.TeleBot("7660963085:AAHZRKZkV88ocfJ9MrAeBwFr8oIxWrn6X1M")

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Знакомство", callback_data="meet")
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton("Карантин", callback_data="quarantine")
    btn3 = types.InlineKeyboardButton("Совместная готовка", callback_data="cooking")
    btn4 = types.InlineKeyboardButton("Блинчики", callback_data="pancakes")
    btn5 = types.InlineKeyboardButton("Крысы", callback_data="rats")
    btn6 = types.InlineKeyboardButton("Будка", callback_data="booth")
    btn7 = types.InlineKeyboardButton("Поездка в Моксву", callback_data="moscow")
    btn8 = types.InlineKeyboardButton("Поездка на море", callback_data="sea")
    btn9 = types.InlineKeyboardButton("Том Ям на КГ", callback_data="soup")
    btn10 = types.InlineKeyboardButton("завели Боску", callback_data="dog")
    btn11 = types.InlineKeyboardButton("Питер", callback_data="piter")
    btn12 = types.InlineKeyboardButton("Ярославль", callback_data="yaroslavl")
    btn13 = types.InlineKeyboardButton("Волга", callback_data="volga")
    btn14 = types.InlineKeyboardButton("Дверь", callback_data="door")
    btn15 = types.InlineKeyboardButton("Расстояние", callback_data="distance")
    btn16 = types.InlineKeyboardButton("Переезд в Москву", callback_data="moving")
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    markup.add(btn6)
    markup.add(btn7)
    markup.add(btn8)
    markup.add(btn9)
    markup.add(btn10)
    markup.add(btn11)
    markup.add(btn12)
    markup.add(btn13)
    markup.add(btn14)
    markup.add(btn15)
    markup.add(btn16)
    
    bot.send_message(message.chat.id, "Куку, Егорик, тут собраны наши воспоминания за все совместные года. Теперь мы всегда можем прийти сюда и посмотреть как все было.", reply_markup=markup)
    
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "Куку, Егорик, тут собраны наши воспоминания за все совместные года. Теперь мы всегда можем прийти сюда и посмотреть как все было.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def on_click(call):
    if call.data == "meet":
        # Отправка текста
        text = (
            "Знакомство:\n"
            "Мы были знакомы давно, ходили же на танцы вместе в детстве, потом мы ходили гулять один раз компанией, "
            "но написал ты мне в 2019 году в апреле и позвал гулять, я в тебя втюрилась с первого раза ахахаха\n"
            "Ты потом куда-то пропадал и окончательно начали общаться мы только с 4 декабря 2019. "
            "В этот день мы говорили с тобой в парке очень долго, шел снег, было здорово, я наврала дома, "
            "что пошла к однокласснице, а сама болтала с тобой, до тебя я никогда и ни с кем не ощущала такого, "
            "что человек «мой», что я хочу проводить все свое время с тобой, что я хочу разговаривать о чем угодно с тобой, "
            "мне было приятно, что ты слушал. Так и началась наша история.\n"
            "Первое фото - самое первое наше совместное фото, которое ты сделал на мой телефон на площадке сзади 4 школы, "
            "мы в те времена очень долго гуляли несмотря на погоду, мерзли, но думаю нам было все равно на это)\n"
            "По-моему в этот же день я поцеловала тебя в щечку на прощанье)\n"
            "Второе фото - сделано 26 декабря 2019 года, в этот день ты меня поцеловал, а я начала говорить, "
            "что не умею целоваться, потому что никогда этого не делала, я до сих пор помню все свои ощущения в тот момент\n"
            "Именно эту фотку я поставила себе на заставку экрана и она стояла больше года точно, выстрелил в меня своей любовью\n"
            "Третье фото - я приходила к тебе в гости, мы делали тебе маску с пандой и говорили о будущем, о поступлении\n"
            "Четвертое фото - мы дурачились у меня дома после какой-то школьной игры, я помню как для общего фото ты встал "
            "рядом со мной сам, тогда мне было очень приятно, что тебе хочется быть рядом со мной даже в таких мелочах"
        )
        bot.send_message(call.message.chat.id, text)

        # Отправка группы фото
        media = [
            types.InputMediaPhoto(open("photo_2025-03-24 23.14.41.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-24 23.14.48.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-24 23.14.51.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-24 23.14.56.jpeg", "rb"))
        ]
        bot.send_media_group(call.message.chat.id, media)

    elif call.data == "quarantine":
        text = (
            "в апреле 2020 года нас всех посадили на карантин, а ты ездил к мне домой на велосипеде, а я тебя всегда ждала, мы забили на учебу и были драгу с другом, очень много разговаривали, валялись, целовались, начали вместе ночевать, много мечтали о будущем, рассуждали о том, как все будет, а еще играли с сонькой вместе и смотрели фильмы и много чего еще делали"
        )
        bot.send_message(call.message.chat.id, text)

        media = [
            types.InputMediaPhoto(open("photo_2025-03-25 00.48.47.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 00.48.30.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 00.48.35.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 00.48.40.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 00.48.23.jpeg", "rb")),
        ]
        bot.send_media_group(call.message.chat.id, media)


    elif call.data == "cooking":
        text = "когда мы только начали встречаться мы очень часто готовили вместе, вареники, манты, чизкейк, морковный пирог, пончики и много разного еще Сейчас мы тоже готовим, но реже, вот например, недавно пельмешки лепили"

        bot.send_message(call.message.chat.id, text)

        media = [
            types.InputMediaPhoto(open("photo_2025-03-25 20.55.36.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 20.55.49.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 20.55.54.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 20.55.59.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 20.56.04.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 20.56.09.jpeg", "rb")),
        ]
        bot.send_media_group(call.message.chat.id, media)

    elif call.data == "pancakes":
        text = "помню я у тебя ночевала и утром сказала, что очень хочу блинчиков, потом ты куда-то молча ушел, а когда я вила на кухню ты готовила для меня блинчики, это было очень и очень приятно, я так тебя люблю"

        bot.send_message(call.message.chat.id, text)

        media = [
            types.InputMediaPhoto(open("photo_2025-03-25 21.02.34.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.02.40.jpeg", "rb")),
        ]
        bot.send_media_group(call.message.chat.id, media)

    elif call.data == "rats":
        text = ("на 14 февраля ты сделал мне важный подарок, я хотела завести себе крысу, но мама не разрешала, это все было на уровне мечты, я знала, что она не разрешит, как и собаку очень долгое время не разрешала, и вот ты приносишь мне клетку, крыс, корм, в общем то все все все, что нужно, "
                "словами не передать, что я чувствую к тебе, ведь ты тот, кто всегда прислушивается к моим желаниям, моим мечтам, ты их исполняешь, знаешь, говорят в народе, что есть волшебник, а есть сказочник, так вот ты, точно волшебник, самый классный, немногословный, но человек дела."
                "Вообще хочу сказать, что ты был единственным, кто тогда поддерживал мои увлечения макияжами, я помню как ты хотел, чтобы я пошла к твоим родителям, а я была со стразами на глазах и сказала, что тогда мне надо их отклеить, а ты в ответ сказал, что тогда это буду уже не я и так я "
                 "поборола страх и пошла со стразами, мне кажется эти твои слова дорогого стоят. Я тебя очень сильно люблю."
                "На фотках как раз крыски, а еще тут ты по Нокиа звонишь куда-то, а еще мы снова дурачимся, еще есть фото как я прогуливала уроки у тебя дома, просто с тобой всегда было так хорошо и сейчас есть."
                )
        bot.send_message(call.message.chat.id, text)
        
        media = [
            types.InputMediaPhoto(open("photo_2025-03-25 21.10.39.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.10.49.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.10.54.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.10.58.jpeg", "rb")),
        ]
        bot.send_media_group(call.message.chat.id, media)

    elif call.data == "booth":
        text = ( "ты затеял построить будку для Тумана, а я тебя поддержала, ты даже построил 3Д-модель на компьютере, этот твой поступок показал мне то, как сильно ты ценишь животных и любишь их, ты очень добрый и нежный, хотя нечасто это показываешь, это видно по твоим поступкам."
                 "Вот так ты потратил все деньги за медаль на то, чтобы купить нужные материалы и начал делать, а я ходила с тобой, ты работал, я читала вслух тебе «Иуда» Андреева, сидя рядом на стуле под навесом. Было так хорошо. С тобой всегда хорошо и спокойно. "
                 "Ты построил офигенную теплую будку для Тумана, думаю он был очень и очень рад, а теперь эта будка служит жильем для Лизы, думаю она тебе тоже благодарна ахахахаха"
                 "В тебе есть черта помогать другим, облегчать их жизни, даже животных"
                 )
        bot.send_message(call.message.chat.id, text)

        media = [
            types.InputMediaPhoto(open("photo_2025-03-25 21.16.30.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.16.32.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.16.36.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.16.40.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.16.43.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.16.46.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.16.48.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.16.51.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.16.54.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.17.04.jpeg", "rb")),
       ]
        bot.send_media_group(call.message.chat.id, media)

    elif call.data == "moscow":
          text = ( "мы в августе перед твоим поступлением намылились в Москву, приехали и жили у той чокнутой бабульки, много ходили по Москве,к"
                 "сами готовили, гуляли, честно я не столько помню Москву в эту поездку, но хорошо помню тебя, ты очень красивый и мой самый дорогой сердцу человек"
                 )
          bot.send_message(call.message.chat.id, text)
    
          media = [
            types.InputMediaPhoto(open("photo_2025-03-25 21.42.47.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.42.44.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.42.37.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.42.41.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.42.32.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.42.29.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.42.26.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 21.42.35.jpeg", "rb")),
        ]
          bot.send_media_group(call.message.chat.id, media)

    elif call.data == "sea":
       text = ( " а еще в 22 году после 1 курса мы поехали на море с твоими родителями и Иришкой"
              "Ели шашлык, каждый день купались, ходили гулять поздно вечером, играли с Иркой," 
              "успели съездить в Абхазию и в горы!"
              )
       bot.send_message(call.message.chat.id, text)

       media = [
           types.InputMediaPhoto(open("photo_2025-03-25 22.45.01.jpeg", "rb")),
           types.InputMediaPhoto(open("photo_2025-03-25 22.45.05.jpeg", "rb")),
           types.InputMediaPhoto(open("photo_2025-03-25 22.45.07.jpeg", "rb")),
           types.InputMediaPhoto(open("photo_2025-03-25 22.45.09.jpeg", "rb")),
           types.InputMediaPhoto(open("photo_2025-03-25 22.45.13.jpeg", "rb")),
           types.InputMediaPhoto(open("photo_2025-03-25 22.45.15.jpeg", "rb")),
           types.InputMediaPhoto(open("photo_2025-03-25 22.45.18.jpeg", "rb")),
           types.InputMediaPhoto(open("photo_2025-03-25 22.45.21.jpeg", "rb")),
           types.InputMediaPhoto(open("photo_2025-03-25 22.45.24.jpeg", "rb")),
           types.InputMediaPhoto(open("photo_2025-03-25 22.44.57.jpeg", "rb")),
       ]
       bot.send_media_group(call.message.chat.id, media)

    elif call.data == "soup":
        text = "с момента поездки в Москву в 21 года перед моим поступлением мы открыли для себя центральный рынок на Китай городе и Том ям, с того момента мы постоянно ездили туда что-то праздновать или просто отдохнуть, мы были там так много раз, что я уже считаю это место нашим, сейчас мы там бываем очень редко, но я это место очень люблю!"

        bot.send_message(call.message.chat.id, text)

        media = [
             types.InputMediaPhoto(open("photo_2025-03-25 23.16.18.jpeg", "rb")),
             types.InputMediaPhoto(open("photo_2025-03-25 23.16.15.jpeg", "rb")),
             types.InputMediaPhoto(open("photo_2025-03-25 23.16.12.jpeg", "rb")),
             types.InputMediaPhoto(open("photo_2025-03-25 23.16.06.jpeg", "rb")),
             types.InputMediaPhoto(open("photo_2025-03-25 23.16.04.jpeg", "rb")),
             types.InputMediaPhoto(open("photo_2025-03-25 23.16.09.jpeg", "rb")),
             types.InputMediaPhoto(open("photo_2025-03-25 23.15.59.jpeg", "rb")),
       ]
        bot.send_media_group(call.message.chat.id, media)

    elif call.data == "dog":
        text = "еще одна моя мечта с детства - собака, и, конечно, тот кто ее осуществил это ты, ты подарил мне сертификат ля покупки бульдога и спустя 1,5 года я его использовала и мы купили босечку, хоть мы часто шутим или может как-то спорим, я считаю что это все же НАША собака, мы любим ее оба и оба ее родители и хозяева, она у нас балбеска, но любимка"

        bot.send_message(call.message.chat.id, text)

        media = [
            types.InputMediaPhoto(open("photo_2025-03-25 23.21.01.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 23.21.05.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 23.21.09.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 23.21.12.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 23.21.14.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 23.21.17.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 23.21.21.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-25 23.26.06.jpeg", "rb")),
       ]
        
        bot.send_media_group(call.message.chat.id, media)

    elif call.data == "piter":
         text = "этим летом побывали в Питере, катались на сапах, но в основном мы там ели ахаххахаха"

         bot.send_message(call.message.chat.id, text)

         media = [
                  types.InputMediaPhoto(open("photo_2025-03-25 23.25.35.jpeg", "rb")),
                  types.InputMediaPhoto(open("photo_2025-03-25 23.25.38.jpeg", "rb")),
                  types.InputMediaPhoto(open("photo_2025-03-25 23.25.43.jpeg", "rb")),
                  types.InputMediaPhoto(open("photo_2025-03-25 23.25.45.jpeg", "rb")),
                  types.InputMediaPhoto(open("photo_2025-03-25 23.25.49.jpeg", "rb")),
        ]
         bot.send_media_group(call.message.chat.id, media)

    elif call.data == "yaroslavl":
         text = "одно из моих любимых воспоминаний, мы долго не виделись, ты делал Волгу, а я училась, и вот мы встретились в Ярославле, жили в отеле несколько дней, очень много гуляли, сходили на выставку! Было классно, любовно, хорошо"

         bot.send_message(call.message.chat.id, text)

         media = [
              types.InputMediaPhoto(open("photo_2025-03-26 12.51.53.jpeg", "rb")),
              types.InputMediaPhoto(open("photo_2025-03-26 12.51.56.jpeg", "rb")),
              types.InputMediaPhoto(open("photo_2025-03-26 12.51.58.jpeg", "rb")),
              types.InputMediaPhoto(open("photo_2025-03-26 12.52.04.jpeg", "rb")),
              types.InputMediaPhoto(open("photo_2025-03-26 12.52.07.jpeg", "rb")),
        ]
         bot.send_media_group(call.message.chat.id, media)

    elif call.data == "door":
        text = "я очень хотела покрасить свою дверь в комнате, в коровий принт, а ты взял и принес мне краску и мы вместе покрасили мою дверь, это была хитрая уловка, чтобы заманить меня к себе и у тебя получилось ахахахахах"

        bot.send_message(call.message.chat.id, text)

        media = [
            types.InputMediaPhoto(open("photo_2025-03-26 12.57.43.jpeg", "rb")),
        ]
        bot.send_media_group(call.message.chat.id, media)

    elif call.data == "volga":
       text = "помню как ты захотел купить себе Волгу, мне очень понравилось эта машина, нас отговаривали все, а мы хотели, нам она очень нравилась и вот так с 2021 года у тебя есть машина, которой ты занимаешься, делаешь классные вещи, ремонтируешь ее сам, разрабатываешь новые штуки, штуки на лазере, разбираешься как это все работает и не сдаешься, у тебя будет самая крутая волга и все твои идеи насчет нее необычные, например мотор, все ведь до сих пор в шоке ходят ахахаха, а это они еще твои 3Д модели не видели!!! А еще я помню как ты меня на ней из школы забирал в мае 11 класса"
       bot.send_message(call.message.chat.id, text)

       media = [
           types.InputMediaPhoto(open("photo_2025-03-26 13.00.57.jpeg", "rb")),
           types.InputMediaPhoto(open("photo_2025-03-26 13.01.02.jpeg", "rb")),
           types.InputMediaPhoto(open("photo_2025-03-26 13.00.52.jpeg", "rb")),
           types.InputMediaPhoto(open("photo_2025-03-26 13.00.39.jpeg", "rb")),
           types.InputMediaPhoto(open("photo_2025-03-26 13.00.35.jpeg", "rb")),
           types.InputMediaPhoto(open("photo_2025-03-26 13.00.32.jpeg", "rb")),
           types.InputMediaPhoto(open("photo_2025-03-26 13.00.47.jpeg", "rb")),
           types.InputMediaPhoto(open("photo_2025-03-26 13.00.43.jpeg", "rb")),
       ]
       bot.send_media_group(call.message.chat.id, media)

    elif call.data == "moving":
        text = ("затем поступила в Москву и я, мы начали совместно жить, прям совсем совсем одни, не считая злую женщину в соседней комнате ахахаха"
              "Мы обустраивали свой быт, было здорово начать жить совсем одним, думаю тогда у нас все еще продолжался конфетного-букетный период так называемый ахахаха он у нас и вправду был дольше чем по статистике ахахаха"
              "Было весело, к нам даже приезжали Кирилл, Сончис, моя мама"
              )
        bot.send_message(call.message.chat.id, text)

        media = [
             types.InputMediaPhoto(open("photo_2025-03-26 13.07.17.jpeg", "rb")),
             types.InputMediaPhoto(open("photo_2025-03-26 13.07.21.jpeg", "rb")),
             types.InputMediaPhoto(open("photo_2025-03-26 13.07.24.jpeg", "rb")),
             types.InputMediaPhoto(open("photo_2025-03-26 13.07.29.jpeg", "rb")),
             types.InputMediaPhoto(open("photo_2025-03-26 13.07.33.jpeg", "rb")),
             types.InputMediaPhoto(open("photo_2025-03-26 13.07.40.jpeg", "rb")),
             types.InputMediaPhoto(open("photo_2025-03-26 13.07.37.jpeg", "rb")),
             types.InputMediaPhoto(open("photo_2025-03-26 13.07.45.jpeg", "rb")),
        ]
        bot.send_media_group(call.message.chat.id, media)

    elif call.data == "distance":
        text = ("после поездки в Москву ты остался там, потому что поступил учиться, мы постоянно чуть ли не каждый день созванивались, а еще ездили друг к другу, ты ко мне на выходные, а к тебе на каникулы, я всегда так тебя ждала и жду сейчас из Тейково, поменялись местами ахахаха "
                "Помню, как мы могли просто спать на созвоне, так хотелось быть вместе"
                )
        bot.send_message(call.message.chat.id, text)

        media = [
            types.InputMediaPhoto(open("photo_2025-03-26 13.12.47.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-26 13.12.53.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-26 13.12.57.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-26 13.13.00.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-26 13.13.03.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-26 13.13.06.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-26 13.13.09.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-26 13.13.12.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-26 13.13.15.jpeg", "rb")),
            types.InputMediaPhoto(open("photo_2025-03-26 13.13.17.jpeg", "rb")),
        ]
        bot.send_media_group(call.message.chat.id, media)


bot.infinity_polling(allowed_updates=["message", "callback_query"])