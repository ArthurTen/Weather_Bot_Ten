import telebot
import requests
import json
bot = telebot.TeleBot('7637677430:AAFqwUNrjBcCayXdhCMPcIHFnlC_eiGPgj0')
API = 'a89d8d5ca85c51c910f4f2df0de9fef6'
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, напиши название города!')
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        tmprtr = int(round(data["main"]["temp"], 0))
        wndspd = round(data["wind"]["speed"], 1)
    else:
        bot.reply_to(message, 'Нет такого города!')

    bot.reply_to(message, f"Сейчас в этом городе температура: {tmprtr}°C \n"
                          f"Влажность: {data['main']['humidity']}%\nСкорость ветра: {wndspd} м/с\n"
                          f"{data['weather'][0]['description']}")
bot.polling(none_stop=True)