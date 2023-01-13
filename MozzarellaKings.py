import telebot
from telebot import types
token = "5978245240:AAFcgBaoLTjM6FhE35bjMlppcv1joaOl0bc"
bot = telebot.TeleBot(token=token)
what = 'Здравствуйте!!! Что желаете заказать?'

@bot.message_handler(commands=['start'])
def echo(message):
    text = message.text
    user = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton('🍕Сделать заказ🍕')
    btn1 = types.KeyboardButton('🔥Готовка пиццы🔥')
    btn2 = types.KeyboardButton('🍾Меню🍾')
    markup.add(btn, btn1, btn2)
    bot.send_message(user, 'Что желаете заказать, {0.first_name}?'.format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def bot_message(message):

    if message.text == '🍾Меню🍾':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        bot.send_message(message.chat.id, 'Веганская пицца')
        bot.send_photo(message.chat.id, 'https://yandex.ru/images/search?from=tabbar&text=укроп&pos=1&img_url=http%3A%2F%2Fw7.pngwing.com%2Fpngs%2F161%2F956%2Fpng-transparent-dill-montreal-style-smoked-meat-dill-food-grass-vegetables.png&rpt=simage&lr=117950')

        bot.send_message(message.chat.id, 'Пицца с мясным ассорти без мясного ассорти')
        bot.send_photo(message.chat.id, 'https://yandex.ru/images/search?from=tabbar&text=пицца%20без%20начинки&pos=27&img_url=http%3A%2F%2Fprintnatkani.ru%2Fuserfiles%2Fshop%2Flarge%2F3221_podushka-pitstsa.jpg&rpt=simage&lr=117950')

        bot.send_message(message.chat.id, 'Хреновая пицца')
        bot.send_photo(message.chat.id, 'https://yandex.ru/images/search?cbir_id=7234335%2F8RHAx1E_F85-6ZAy5pH3sA1021&pos=0&rpt=imageview&img_url=http%3A%2F%2Fmedia.patriots.win%2Fpost%2F5v2xltU3.jpeg&cbird=91&cbir_page=similar&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F7234335%2F8RHAx1E_F85-6ZAy5pH3sA1021%2Forig')

        bot.send_message(message.chat.id, 'Трамп пицца')
        bot.send_photo(message.chat.id, 'https://yandex.ru/images/search?text=пицца%20смешная&from=tabbar&p=2&pos=81&rpt=simage&img_url=http%3A%2F%2Fi.imgur.com%2FxiCjMtI.jpg&lr=117950')

        bot.send_message(message.chat.id, '🍾Меню🍾', reply_markup= markup)

# поллинг - вечный цикл с обновлением входящих сообщений
bot.polling(none_stop=True)

