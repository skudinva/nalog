from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
import bo_search as bo
import sys

if len(sys.argv) > 1:
    c_token = sys.argv[1]
else:
    tFile = open('./tBot.token', 'r')
    c_token = tFile.read()
    tFile.close()

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Напиши наименование организации')

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(bo.parse_result(update.message.text))

def main():
    updater = Updater(c_token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    #dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
