import telebot

from telebot import types

bot = telebot.TeleBot('6162614819:AAH2oRoILxujee41cOeCV2Bgx3dFKnMzvsU')

@bot.message_handler(commands=['start' , 'help'])
def main(message):
    keyboard = types.InlineKeyboardMarkup()
    markup = types.InlineKeyboardMarkup(row_width=1)
    url_btn  = types.InlineKeyboardButton(text= "Выпуск 2015" , url ="https://t.me/+WZMBLCXuyXsyYWQy")
    url_btn1 = types.InlineKeyboardButton(text= "Выпуск 2016" , url ="https://t.me/+UeyRRlwZf5wxYzM6")
    url_btn2 = types.InlineKeyboardButton(text= "Выпуск 2017" , url ="https://t.me/+5mvRVfj9WYQzNDRi")
    url_btn3 = types.InlineKeyboardButton(text= "Выпуск 2018" , url ="https://t.me/+pcxA8u4EnK5hMmUy")
    url_btn4 = types.InlineKeyboardButton(text= "Выпуск 2019" , url ="https://t.me/+OaS4lYTiQtkwNmVi")
    url_btn5 = types.InlineKeyboardButton(text= "Выпуск 2020" , url ="https://t.me/+blZadIajGAM4YzZi")
    url_btn6 = types.InlineKeyboardButton(text= "Выпуск 2021" , url ="https://t.me/+x9BCWzU2xfA0NzQy")
    url_btn7 = types.InlineKeyboardButton(text= "Выпуск 2022" , url ="https://t.me/+zGLE9cBo_jw2NjU6")
    
 
    keyboard.add(url_btn)
    keyboard.add(url_btn1)
    keyboard.add(url_btn2)
    keyboard.add(url_btn3)
    keyboard.add(url_btn4)
    keyboard.add(url_btn5)
    keyboard.add(url_btn6)
    keyboard.add(url_btn7)
   

    
    bot.send_message(message.chat.id, "Приветствуем, выпускники КБТУ! Наш телеграмм бот создан для того, чтобы вы могли оставаться на связи с бывшими однокурсниками и коллегами. Вы найдете группы для выпускников по годам, где можно общаться, делиться новостями и опытом. Мы желаем вам множество ярких моментов в новом этапе вашей жизни и надеемся, что наш телеграмм бот станет для вас местом поддержки и взаимопомощи. Присоединяйтесь к нашему дружному сообществу выпускников КБТУ!" , reply_markup = keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)