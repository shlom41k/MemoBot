import telebot
import time
from datetime import datetime
import glob
import random
import Stickers
import JSON


global Names

Names = JSON.LoadStat(JSON.savepath)

# Insert your bot token here
shlom41k_bot_token = ""

bot = telebot.TeleBot(shlom41k_bot_token)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('/test', '/getmem', )


@bot.message_handler(commands=['start'])
def start_message(message):
    ans = bot.send_sticker(message.chat.id, Stickers.STIC_PRESS_F[0], reply_markup=keyboard1)
    print("BOT RESPONSE : " + str(datetime.now()) + "\n")


@bot.message_handler(commands=['test'])
def test_message(message):
    try:
        global Names
        #print("BOT REQUEST: " + str(datetime.now()) + "\n" + str(message))
        print("{0}: BOT REQUEST - from {1} {2} [{3}]: '{4}'".format(str(datetime.now()), str(message.from_user.first_name),
                                                        str(message.from_user.last_name), str(message.from_user.username),
                                                        str(message.text)))
        ans = bot.send_sticker(message.chat.id, random.choice(Stickers.STIC_PRESS_F))
        print("{0}: BOT RESPONSE - to {1} {2} [{3}]".format(str(datetime.now()), str(message.from_user.first_name),
                                                         str(message.from_user.last_name),
                                                         str(message.from_user.username)))
        Names = JSON.UpdateStat(JSON.savepath, Names, "{0} {1} {2}".format(str(message.from_user.first_name),
                                                         str(message.from_user.last_name),
                                                         str(message.from_user.username)), str(message.text))
    except Exception as e:
        print("Error, when get command {0}".format(str(message.text)))
        print(e)


@bot.message_handler(commands=['getmem'])
def getpic_message(message):
    global Names
    try:
        print("{0}: BOT REQUEST - from {1} {2} [{3}]: '{4}'".format(str(datetime.now()), str(message.from_user.first_name),
                                                                    str(message.from_user.last_name),
                                                                    str(message.from_user.username),
                                                                    str(message.text)))
        list = glob.glob("files\memchiki\*.*")
        photo = open(list[random.randrange(0, list.__len__())], 'rb')
        ans = bot.send_photo(message.chat.id, photo)
        print("{0}: BOT RESPONSE - to {1} {2} [{3}]".format(str(datetime.now()), str(message.from_user.first_name),
                                                            str(message.from_user.last_name),
                                                            str(message.from_user.username)))
        Names = JSON.UpdateStat(JSON.savepath, Names, "{0} {1} {2}".format(str(message.from_user.first_name),
                                                                           str(message.from_user.last_name),
                                                                           str(message.from_user.username)),
                                                                            str(message.text))
    except Exception as e:
        print("Error, when get command {0}".format(str(message.text)))
        print(e)


@bot.message_handler(content_types=['text'])
def send_text(message):
    global Names
    try:
        print("{0}: BOT REQUEST - from {1} {2} [{3}]: '{4}'".format(str(datetime.now()), str(message.from_user.first_name),
                                                                    str(message.from_user.last_name),
                                                                    str(message.from_user.username),
                                                                    str(message.text)))
        ans = ""
        if message.text.lower() == 'привет':
            ans = bot.send_message(message.chat.id, 'Привет, мой создатель')
        elif message.text.lower() == 'пока':
            ans = bot.send_message(message.chat.id, 'Прощай, создатель')
        elif message.text.lower() == 'я тебя люблю':
            ans = bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
        print("{0}: BOT RESPONSE - to {1} {2} [{3}]".format(str(datetime.now()), str(message.from_user.first_name),
                                                            str(message.from_user.last_name),
                                                            str(message.from_user.username)))
        Names = JSON.UpdateStat(JSON.savepath, Names, "{0} {1} {2}".format(str(message.from_user.first_name),
                                                                           str(message.from_user.last_name),
                                                                           str(message.from_user.username)),
                                                                            str(message.text))
    except Exception as e:
        print("Error, when get message {0}".format(str(message.text)))
        print(e)


@bot.message_handler(content_types=['sticker', ])
def sticker_id(message):
    print("BOT REQUEST: " + str(datetime.now()) + "\n" + str(message))


while True:
    print("{0}: BOT STARTED".format(str(datetime.now())))
    try:
        bot.polling(none_stop=True, interval=1)

    except Exception as e:
        print(e)
        print("{0}: BOT STOPPED".format(str(datetime.now())))
        time.sleep(10)
