import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Ваш токен бота
API_TOKEN = "7614502051:AAFVlWZCajhEcTtYb9SoJbKpAtR53uQWUcQ"

# Создаём экземпляр бота
bot = telebot.TeleBot(API_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаём клавиатуру с кнопкой для веб-приложения
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="Открыть Chainhash",
            web_app=WebAppInfo(url="https://chainqwerty.github.io/myopicHAINSSS/")  # Укажите свой URL
        )
    )
    # Отправляем приветственное сообщение
    bot.send_message(
        chat_id=message.chat.id,
        text="Добро пожаловать в #Chainhash! 🚀\nНажмите кнопку ниже, чтобы открыть приложение:",
        reply_markup=keyboard
    )

# Запуск бота
bot.polling()
