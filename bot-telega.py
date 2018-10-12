import config
import telebot
import random 

bot = telebot.TeleBot(config.token)



@bot.message_handler(commands=['ruletka'])
def handle_RUletka(message):
	z = 0
	true = True
	while true:
		y = random.randint(0,6)
		x = random.randint(0,6)
		
		if x != y:
			sayiflife = random.randint(0,3)
			iflife = ["Wow", "Крутой(ая)", "Пффф, повезло", "В следующий раз может не повезти"]
			bot.send_message(message.chat.id, iflife[sayiflife])
			print("x = ",x)
			print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
			print("y = ",y)
			z += 1
		if  x == y:
			bot.send_message(message.chat.id, "Ты проиграл(ла)")
			z = 0
			true = False
		if  z == 6:
			bot.send_message(message.chat.id, "Ты победил(ла)")
			z = 0
			true = False

#@bot.message_handler(content_types=["text"])
#def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
#    
#   	bot.send_message(message.chat.id, message.text + " LOL")

	


if __name__ == '__main__':
	 bot.polling(none_stop=True)