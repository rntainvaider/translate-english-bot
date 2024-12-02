import random
import telebot
from telebot import types
from telebot.handler_backends import StatesGroup, State


class Command:
    ADD_WORD = "Добавить слово ➕"
    DELETE_WORD = "Удалить слово🔙"
    NEXT = "Дальше ⏭"


class MyStates(StatesGroup):
    target_word = State()
    translate_word = State()
    another_words = State()


def register_handlers(bot: telebot) -> None:
    @bot.message_handler(commands=["start"])
    def send_welcome(message) -> None:
        bot.send_message(
            message.chat.id,
            "Привет 👋 Давай попрактикуемся в английском языке. Тренировки можешь проходить в удобном для себя темпе.",
        )

        markup = types.ReplyKeyboardMarkup(row_width=2)
        translate = "Мир"
        target_word = "Peace"
        target_word_btn = types.KeyboardButton(target_word)
        other_words = ["Green", "Car", "Hello"]
        other_words_btn = [types.KeyboardButton(word) for word in other_words]

        buttons = [target_word_btn] + other_words_btn
        random.shuffle(buttons)

        next_btn = types.KeyboardButton(Command.NEXT)
        add_word_btn = types.KeyboardButton(Command.ADD_WORD)
        delete_word_btn = types.KeyboardButton(Command.DELETE_WORD)
        buttons.extend([next_btn, add_word_btn, delete_word_btn])

        markup.add(*buttons)

        bot.send_message(
            message.chat.id, f"Угадай слово {translate}", reply_markup=markup
        )

        bot.set_state(message.from_user.id, MyStates.target_word, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["target_word"] = target_word
            data["translate_word"] = translate
            data["other_words"] = other_words

    @bot.message_handler(func=lambda message: True, content_types=["text"])
    def message_reply(message) -> None:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            target_word = data["target_word"]
        if message.text == target_word:
            bot.send_message(message.chat.id, "Всё правильно")
        else:
            bot.send_message(message.chat.id, "Неправильно. Попробуй снова!")
