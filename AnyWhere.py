import telebot
import sys
import subprocess
import time

API_KEY = "5476384919:AAH1qm_tXg6xFWAWjc8fy6fUI0JeP-NA52A"
bot = telebot.TeleBot(API_KEY, parse_mode = None)

def is_admin(message):
  admins = [5392734097, 983035043]
  return message.chat.id == (admins[0] or admins[1])

@bot.message_handler(func=is_admin, commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '😇 *Знакомство*\n\nЭтот бот предназначен для управления моего собственного VDS и т. п.\n_*Работает только с ID владельца_', parse_mode="Markdown")

@bot.message_handler(func=is_admin, commands=['py'])
def py_func(message):
  try:
    exec(message.text.replace('/py ', '', 1))
  except:
    e = sys.exc_info()[1]
    bot.send_message(message.chat.id, '*[ ! ]* Произошла ошибка!\n\n'+e.args[0], parse_mode="Markdown")

@bot.message_handler(func=is_admin, content_types=['document'])
def get_file(message):
  path = message.caption
  file_name = message.document.file_name
  file_id = message.document.file_name
  file_id_info = bot.get_file(message.document.file_id)

  downloaded_file = bot.download_file(file_id_info.file_path)
  with open(path, 'wb') as new_file:
    new_file.write(downloaded_file)
  bot.reply_to(message, "[ ! ] Файл успешно загружен.")
  
@bot.message_handler(func=is_admin, content_types='text')
def get_message(message):
  result = subprocess.run(message.text, capture_output=True, text=True)
  bot.send_message(message.chat.id, result.stdout+"\n\n"+result.stderr, parse_mode="Markdown")
  
while True:
  try:
    bot.polling(none_stop=True, interval=2) 
    break
  except:
    bot.stop_polling()
    time.sleep(15)
