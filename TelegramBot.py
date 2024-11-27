import telebot
import webbrowser

bot = telebot.TeleBot('7972137837:AAHjsNoxlogcQYXeEECIBuD31u-oQN8D3Do')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://itproger.com')



@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'id: {message.from_user.id}')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b><em>Информация</em></b>', parse_mode='html') # форматирование текста в режиме html

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'id: {message.from_user.id}')


bot.polling(non_stop=True)
