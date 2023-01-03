# import everything
from flask import Flask, request
import telegram.ext
from telebot.credentials import bot_token, bot_user_name, api_key
import openai

openai.api_key = api_key
import logging

global TOKEN
TOKEN = bot_token

updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

base_prompt = """
                I'm a 3-year-old and please answer questions on the blockchain. Use simple language I can understand:

                """


def start(update, context):
    update.message.reply_text("Hey there 👋! Welcome to BlockLearn")


def help(update, context):
    update.message.reply_text(
        """
        My goal is to help you learn Blockchain.

        /start -> Welcome to the BlockLearn
        /help -> This particular message
        /content -> About various Playlist
        /Python -> The first video from Python playlist
        """
    )

    
def content(update, context):
    update.message.reply_text(
        """
        We have various playlist and articles available
        Lesson1: What is Blockchain?
            1.1 Life Before Blockchain
            1.2 Now Blockchain
            1.3 The Future
        """
    )


def Lesson1(update, context):
    update.message.reply_text(
        """
        Suppose you are transferring money to your family or friends
        from your bank account.You would log in to online banking and
        transfer the amount to the other person using their account number. 
        """
    )
    update.message.reply_text(
        """ 
        When the transaction is done,your bank updates the transaction records. 
        It seems simple enough, right? There is a potential issue which most of us neglect.
        """
    )
    update.message.reply_text(
        """ 
        These types of transactions can be tampered with very quickly.But this 
        vulnerability is essentially why Blockchain technology was created.
        """
    )


def Query(update, context):
    update.message.reply_text("Hey there 👋! Welcome to BlockLearn")


dispatcher.add_handler(telegram.ext.CommandHandler("start", start))
dispatcher.add_handler(telegram.ext.CommandHandler("content", content))
dispatcher.add_handler(telegram.ext.CommandHandler("help", help))
dispatcher.add_handler(telegram.ext.CommandHandler("Lesson1", Lesson1))
dispatcher.add_handler(telegram.ext.CommandHandler("Query", Query))

updater.start_polling()
updater.idle()
