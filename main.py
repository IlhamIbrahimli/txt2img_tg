from config import *
import classes
import telebot
import sqlite3

bot = telebot.TeleBot(TOKEN)
api = classes.Text2ImageAPI('https://api-key.fusionbrain.ai/', API_KEY, SECRET_KEY)


@bot.message_handler(commands=['generate_img'])
def largest_area(message):
    n = telebot.util.extract_arguments(message.text)
    model_id = api.get_model()
    uuid = api.generate(n, model_id)
    images = api.check_generation(uuid)[0]
    b64_str = images
    api.return_generated_image(b64_str,f"{message.chat.id}.png")
    bot.send_photo(message.chat.id,photo=open(f"./{message.chat.id}.png","rb"))

    

bot.infinity_polling()
