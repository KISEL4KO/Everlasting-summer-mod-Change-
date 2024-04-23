init:
    $ mods["prologue123"] = u"Change"
    image gorod  = "mods/120/backgrounds/gorod.png"
    image buss =  "mods/120/backgrounds/buss.png"
    $ bg_sound1 = "mods/120/sounds/bg_sound1.mp3"
    $ bg_sound2 = "mods/120/sounds/bg_sound2.mp3"



#start prologue
label prologue123:
     
   
    #Author words
    "Вечер пришел незаметно, фонари только-только начали просыпаться на улице."
    play music bg_sound1
    
    #chage bg
    scene gorod with dissolve
    "Нашему Семёну пришлось идти в ночную смену работать на завод. Ничего не поделаешь... 
    начальство требует явиться, так как другой человек не смог явиться по каким-то причинам."

    #Semen words
    me"Ага, конечно. Небось бухает снова, а мне за него отдуваться приходится. 
    Злившись на этого человека и пиная снег"
    "Семён шел по улице уже не надеясь 
    отдохнуть в свой единственный выходной."
    
    #Author words
    "Музыка, которая играла в его наушниках хоть немного, 
    но успокаивала его в этот не столь суровый зимний день.
    Сегодня зима открыто говорила, что она благосклонна к 
    людям и даёт шанс ей насладиться."
    
    "Плеер который он купил себе не так давно оказался 
    полезной и весьма классной штучкой.
    Ночью с музыкой под фонарями и поблескивающим 
    снегом чувствуешь себя странно и... спокойно."
  
    "Да, спокойно, ведь не каждый раз удается застать такой момент, ещё когда работаешь 
    каждый день просто перестаешь замечать какие-либо мелочи. 
    В этих мелочах чувствуется своя особенная атмосфера, 
    такую ни за какие деньги не купишь."
    "Семён начал глупо улыбаться смотря на фонарь и снег который иногда сверкал из-за света. 
    Он всегда был чему-то недоволен и счастливым его было не назвать. 
    Но сейчас он что-то чувствовал." 
    "Чувствовал теплоту на душе и совсем небольшую радость.
    И всё же опоздать не хотелось, поэтому Семён продолжил 
    свой путь к остановке смахнув свою глупую, но настоящую улыбку."

    #bus stop
    scene bg bus_stop
    "Через пару минут он уже стоял на ней, как и автобус под маршрутом 410. 
    Каждый день уже на протяжении нескольких лет Семён ездил на работу в этом автобусе."
    
    #change bg
    scene buss with dissolve
    
    "В этот раз автобус выглядел странным, вроде бы ни чем не отличался, 
    но чувство у Семёна было такое что с автобусом что-то не так."
    
            
    #Semen words
    me"Может просто автобус новый?  Ай, ладно, не буду я заморачиваться всё равно это тот же маршрут."
  
    #change bg
    scene bg int_bus
    #Author words
    "Не долго думая он зашёл в автобус и уселся на первое попавшееся на глаза место. 
    Автобус был пустым и это не удивительно."
    "Кто будет ехать маршрутом который едет на окраину 
    города на последнем сегодня автобусе? Вот я например не знаю."
    "Автобус тронулся, Семён выключил плеер и под звуки гудящего мотора стал зевать." 
    "Он решил немного вздремнуть перед работой и подойдя к водителю попросил разбудить 
    его на последней остановке. Водитель молча кивнул, а Семен уселся по удобнее 
    на своё место стал понемногу засыпать."
    
    #останавливаем музыку
    stop music
    #закрываем глаза
    show blink with dissolve
    #Слова Ольги дмитревны
    mtp"Семен вставай,хватит спать,такими темпами все водные процедуры проспишь,а может еще и линейку."
#показываем дом внутри
    scene bg int_house_of_dv_day
    #показываем злую ольгу дмитревну
    show mt pioneer angry 
    
    
    show unblink with dissolve
    play music bg_sound2
    "Открыв один глаз я посмотрел на недовольную Ольгу Димтриевну."
    
    jump day_sevenMode 

#7day	
label day_sevenMode:
    
    #слова Семена
    me"Хорошо, хорошо, я встаю."
    #показать спокойную Ольгу Димтриевну
    show mt pioneer smile close with dissolve2
    
    mtp"..."
    #показываем дом внутри
    play sound sfx_close_door_1
    scene bg int_house_of_dv_day with dissolve
    "На самом деле вставать мне вовсе не хотелось,но встать всё-же пришлось,конечно под сильными упрёками Ольги Дмитриевны,которые я особо не слышал."
    "Взяв свои умывальные принадлежности, я поплелся к довольно уже привычным умывальникам с ледяной водой."
    scene bg ext_washstand_day with dissolve
    "Около умывальников я встретил славю которая пробегала в сторону домиков."