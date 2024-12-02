import telebot
from config import TOKEN
from handlers.handlers_ import register_handlers


def main() -> None:

    bot = telebot.TeleBot(TOKEN)

    register_handlers(bot)

    print("bot is running")
    bot.polling()


if __name__ == "__main__":
    main()
