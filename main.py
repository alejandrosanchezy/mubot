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
button = tb.types.InlineKeyboardButton('Start', callback_data='start')
markup_start.add(button)

markup_game = tb.types.InlineKeyboardMarkup()
button_one = tb.types.InlineKeyboardButton('Axiom One', callback_data='one')
button_two = tb.types.InlineKeyboardButton('Axiom Two', callback_data='two')
button_three = tb.types.InlineKeyboardButton('Axiom Three', callback_data='three')
button_four = tb.types.InlineKeyboardButton('Axiom Four', callback_data='four')
button_reset = tb.types.InlineKeyboardButton('Reset', callback_data='reset')
markup_game.add(button_one, button_two, button_three, button_four, button_reset)


@bot.message_handler(commands=['start'])
def start(message):
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id, welcome, reply_markup=markup_start)
    except Exception as e:
        logger.exception(e.args)
    finally:
        logger.info('An user is using MUBOT.')


@bot.callback_query_handler(func=lambda call: call.data in ['start'])
def callback_handler_start(call):
    try:
        chat_id = call.message.chat.id
        bot.send_message(chat_id, game.get_state(), reply_markup=markup_game)
    except Exception as e:
        logger.exception(e.args)
    finally:
        logger.info('An user has started a new game.')


@bot.callback_query_handler(func=lambda call: call.data in ['one'])
def callback_handler_axiom_one(call):
    try:
        chat_id = call.message.chat.id
        bot.send_message(chat_id, game.axiom_one(), reply_markup=markup_game)
    except Exception as e:
        logger.exception(e.args)
    finally:
        logger.info('An user has used the axiom one.')


@bot.callback_query_handler(func=lambda call: call.data in ['two'])
def callback_handler_axiom_two(call):
    try:
        chat_id = call.message.chat.id
        bot.send_message(chat_id, game.axiom_two(), reply_markup=markup_game)
    except Exception as e:
        logger.exception(e.args)
    finally:
        logger.info('An user has used the axiom two.')


@bot.callback_query_handler(func=lambda call: call.data in ['three'])
def callback_handler_axiom_three(call):
    try:
        options = game.axiom_three()
        markup_options = tb.types.InlineKeyboardMarkup()
        chat_id = call.message.chat.id
        if bool(game.options_by_axiom_three.keys()):
            for i in list(options.keys()):
                button_i = tb.types.InlineKeyboardButton(str(i) + ') ' + options.get(i), callback_data=str(i))
                markup_options.add(button_i)
            msg = 'Choose an option:'
            bot.send_message(chat_id, msg, reply_markup=markup_options)
        else:
            bot.send_message(chat_id, game.get_state(), reply_markup=markup_game)
    except Exception as e:
        logger.exception(e.args)
    finally:
        logger.info('An user has used the axiom three.')


def handler_apply_axiom_three(call):
    if game.options_by_axiom_three.keys():
        state = call.data in list(game.options_by_axiom_three.keys())
    else:
        state = False
    return state


@bot.callback_query_handler(func=lambda call: handler_apply_axiom_three(call))
def callback_handler_axiom_three(call):
    try:
        chat_id = call.message.chat.id
        bot.send_message(chat_id, game.apply_axiom_three(call.data), reply_markup=markup_game)
    except Exception as e:
        logger.exception(e.args)
    finally:
        logger.info('An user has used the axiom four.')


@bot.callback_query_handler(func=lambda call: call.data in ['four'])
def callback_handler_axiom_four(call):
    try:
        options = game.axiom_four()
        markup_options = tb.types.InlineKeyboardMarkup()
        chat_id = call.message.chat.id
        if bool(game.options_by_axiom_four.keys()):
            for i in list(options.keys()):
                button_i = tb.types.InlineKeyboardButton(str(i) + ') ' + options.get(i), callback_data=str(i))
                markup_options.add(button_i)
            msg = 'Choose an option:'
            bot.send_message(chat_id, msg, reply_markup=markup_options)
        else:
            bot.send_message(chat_id, game.get_state(), reply_markup=markup_game)
    except Exception as e:
        logger.exception(e.args)
    finally:
        logger.info('An user has used the axiom four.')


def handler_apply_axiom_four(call):
    if game.options_by_axiom_four.keys():
        state = call.data in list(game.options_by_axiom_four.keys())
    else:
        state = False
    return state


@bot.callback_query_handler(func=lambda call: handler_apply_axiom_four(call))
def callback_handler_axiom_four(call):
    try:
        chat_id = call.message.chat.id
        bot.send_message(chat_id, game.apply_axiom_four(call.data), reply_markup=markup_game)
    except Exception as e:
        logger.exception(e.args)
    finally:
        logger.info('An user has used the axiom four.')


@bot.callback_query_handler(func=lambda call: call.data in ['reset'])
def callback_handler_reset(call):
    try:
        chat_id = call.message.chat.id
        bot.send_message(chat_id, game.reset(), reply_markup=markup_game)
    except Exception as e:
        logger.exception(e.args)
    finally:
        logger.info('An user reset of the game.')


bot.polling()
