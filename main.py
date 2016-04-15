import telebot
import constants
import os
import random
import urllib.request as urllib2

bot = telebot.TeleBot(constants.token)


#Отправить сообщение от бота
#bot.send_message(56259004,"Privet")
print(bot.get_me())


#НАСТРОЙКА МЕНЮ
@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('фото', 'аудио','документы')
    user_markup.row('стикер', 'видео','голос', 'локация')
    bot.send_message(message.from_user.id, 'Приветствую', reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_text(message):
    hide_markup = telebot.types.ReplyKeyboardHide()
    bot.send_message(message.from_user.id, "..", reply_markup=hide_markup)

@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, "Я пока еще молодой бот.")

@bot.message_handler(content_types=['text'])
#ОТПРАВКА ПРИВЕТОВ
def handle_text(message):

    if message.text == "Привет" or message.text == "Привет.":
       bot.send_message(message.from_user.id, "И тебе привет.")

    elif message.text == "эй привет" or message.text == "Эй привет." or message.text == "Эй привет":
        bot.send_message(message.from_user.id, "Да да, чо надо?")

    elif message.text == "?" and str(message.from_user.id)== "56259004":
        bot.send_message(message.chat.id, "Это же ты")

#ОТПРАВКА РАНДОМНОГО ФОТО
    elif message.text == 'фото':
        directory = 'C:/Users/kapustin/PycharmProjects/Telegrambot/files/photo'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
#ОТПРАВКА РАНДОМНОГО АУДИО
    elif message.text == 'аудио':
        directory = 'C:/Users/kapustin/PycharmProjects/Telegrambot/files/audio'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        audio = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()


#ОТПРАВКА РАНДОМНОГО ДОКУМЕНТА
    elif message.text == 'документы':
        directory = 'C:/Users/kapustin/PycharmProjects/Telegrambot/files/docs'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        doc = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_document')
        bot.send_document(message.from_user.id, doc)
        doc.close()

#ОТПРАВКА СТИКЕРА
    elif message.text == 'стикер':
         bot.send_sticker(message.from_user.id, constants.sticker1)


    else:
            bot.send_message(message.from_user.id, "Все не так")

bot.polling(none_stop=True, interval=0)


