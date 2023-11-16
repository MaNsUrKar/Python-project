import os
import time
import datetime
import pyttsx3
import speech_recognition as sr
from fuzzywuzzy import fuzz

opts={
    "alias": ('Ролакс','Олакс','Ролекс'),
    "tbr":('ответь','скажи','расскажи','найди','переведи','посчитай','произнеси'),
    "cmds":{
        "ctime":('сколько время','какое сейчас время','который сейчас час','какое сейчас время суток','сколько времени','сколько сейчас времени'),
        "radio":('включи музон','вруби музыку','включи музыку','воспроизведи музыку','вруби музон','включи трек', 'поставь трек', 'поставь музыку'),
		  "radiocontrol":('выключи музон','выруби музыку','выключи музыку', 'стоп', 'пауза', 'тише', 'громче', 'следующий трек', 'предыдущий трек'),
        "stupid1":('расскажи анекдот','расскажи шутку','расскажи что нибудь','рассмеши меня','ты знаешь анекдоты')
    }
}
#Функции
def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language= "ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x,"").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x,"").strip()

            #Распознаем и выплняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])


    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")


def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd,x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RS['percent'] = vrt

    return RC

def execute_cmd(cmd):
    if cmd == 'ctime':
        now = datetime.datetime.now()
        speak("Сейчас "+ str(now.hour) + ":" + str(now.minute))

    elif cmd == 'radio':
        os.system("Музыка")
    elif cmd == 'stupid1':
        speak("Мам, смотри, голубь! У тебя хлеб есть? — Без хлеба ешь!")
    else:
        print('Команда не распознана, повторите еще раз')
#Запуск программы
    r = sr.Recognizer()
    m = sr.Microphone(device_index=1)

    with m as sourse:
        r.adjust_for_ambient_noise(sourse)

    speak_engine = pyttsx3.init()

    #только если у вас установлены голоса для синтеза речи
    voices = speak_engine.getProperty('voices')
    speak_engine.getProperty('voice', voices[4].id)

    speak("Доброво времени суток, пользователь")
    speak("Ролакс вас cлушает")

    stop_listening = r.listen_in_background(m, callback)
    while True: time.sleep(0.1)