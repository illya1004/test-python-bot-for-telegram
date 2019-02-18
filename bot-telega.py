import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

user_name = "none"
hack_fish = "none"

@bot.message_handler(commands=['info'])
def handle_INFO(message):
	bot.send_message(message.chat.id, "Привет human\nНапишы команду /buy чтобы оставить заявку на взлом после чего с вами свяжется Админ\n(Цена и все отстаьное обсудиться в ЛС)")
	humnas_id = open("id.txt", "a")
	message.chat.id = str(message.chat.id)
	humnas_id.write(message.chat.id + "\n")
	humnas_id.close()

@bot.message_handler(commands=['buy'])
def send_welcome(message):
	markup = types.InlineKeyboardMarkup()
	url_button1 = types.InlineKeyboardButton(text="Взлом аккаунта", callback_data="hack")
	url_button2 = types.InlineKeyboardButton(text="Фишинг на заказ", callback_data="fish")
	markup.add(url_button1, url_button2) #Имена кнопок
	msg = bot.reply_to(message, 'Виберите товар \n1.Взлом аккаунта в соц.сети \n2.Сделать фишинг на заказ', reply_markup=markup)

	global user_name
	user_name = message.from_user.username

	humnas_id = open("id.txt", "a")
	message.chat.id = str(message.chat.id)
	humnas_id.write(message.chat.id + " " + user_name + "\n")
	humnas_id.close()

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.message:
		if call.data == "hack":
			global hack_fish
			hack_fish = " hack"
			markup2 = types.InlineKeyboardMarkup()
			url_button3 = types.InlineKeyboardButton(text="Контакти", callback_data="contacts")
			markup2.add(url_button3) #Имена кнопок
			bot.send_message(chat_id=call.message.chat.id,text='Укажите контакти для связи (Telegram, jabber или просто нажмите на кнопку ниже)', reply_markup=markup2)
		if call.data == "fish":
			hack_fish = " fish"
			markup2 = types.InlineKeyboardMarkup()
			url_button3 = types.InlineKeyboardButton(text="Контакти", callback_data="contacts")
			markup2.add(url_button3) #Имена кнопок
			bot.send_message(chat_id=call.message.chat.id,text='Укажите контакти для связи (Telegram, jabber или просто нажмите на кнопку ниже)', reply_markup=markup2)
		if call.data == "contacts":
			bot.send_message("384751309", text=user_name + hack_fish)
			bot.send_message(chat_id=call.message.chat.id, text="В скором времени мы с вами свяжемся")

#@bot.message_handler(content_types=["text"])
#def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
#    
#bot.send_message(message.chat.id, message.text + " LOL")

	


if __name__ == '__main__':
	 bot.polling(none_stop=True)
