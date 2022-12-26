# import everything
from flask import Flask, request
import telegram.ext
from telebot.credentials import bot_token, bot_user_name

global TOKEN
TOKEN = bot_token

updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    update.message.reply_text("Hey there! Welcome to BlockLearn")


def help(update, context):
    update.message.reply_text(
        """
        /start -> Welcome to the BlockLearn
        /help -> This particular message
        /context -> About various Playlist
        /Python -> The first video from Python playlist
        """
    )


def content(update, context):
    update.message.reply_text("We have various playlist and articles available")


def Python(update, context):
    update.message.reply_text("Python tutorial link")


dispatcher.add_handler(telegram.ext.CommandHandler("start", start))
dispatcher.add_handler(telegram.ext.CommandHandler("Python", Python))
dispatcher.add_handler(telegram.ext.CommandHandler("help", help))

updater.start_polling()
updater.idle()
