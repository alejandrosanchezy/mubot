import logging
import os
import telebot as tb
from miu import MIU
from msg import welcome

logging.basicConfig(level=logging.DEBUG, filename='miubot.log')
logger = tb.logger
logger.setLevel(logging.DEBUG)

TOKEN_TELEGRAM = os.environ.get('TOKEN')
bot = tb.TeleBot(TOKEN_TELEGRAM, parse_mode=None)
game = MIU()

markup_start = tb.types.InlineKeyboardMarkup()
button = tb.types.InlineKeyboardButton('Start', callback_data='Start')
markup_start.add(button)

markup_game = tb.types.InlineKeyboardMarkup()
button_one = tb.types.InlineKeyboardButton('Axiom One', callback_data='One')
button_two = tb.types.InlineKeyboardButton('Axiom Two', callback_data='Two')
button_three = tb.types.InlineKeyboardButton('Axiom Three', callback_data='Three')
button_four = tb.types.InlineKeyboardButton('Axiom Four', callback_data='Four')
button_reset = tb.types.InlineKeyboardButton('Reset', callback_data='Reset')
markup_game.add(button_one, button_two, button_three, button_four, button_reset)


@bot.message_handler(commands=['start'])
def start(message):
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id, welcome, reply_markup=markup_start)
    except Exception as e:
        logger.exception(e.args)
    finally:
        logger.info('An user is using MIUBOT.')


@bot.callback_query_handler(func=lambda call: call.data in ['Start'])
def callback_handler_start(call):
    try:
        chat_id = call.message.chat.id
        bot.send_message(chat_id, game.get_state(), reply_markup=markup_game)
    except Exception as e:
        logger.exception(e.args)
    finally:
        logger.info('An user has started a new game.')


@bot.callback_query_handler(func=lambda call: call.data in ['One'])
def callback_handler_start(call):
    try:
        chat_id = call.message.chat.id
        bot.send_message(chat_id, game.axiom_one(), reply_markup=markup_game)
    except Exception as e:
        logger.exception(e.args)
    finally:
        logger.info('An user has used the axiom one.')


bot.polling()
