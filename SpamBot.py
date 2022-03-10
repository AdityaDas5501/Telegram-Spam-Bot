from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import time

# Create the Updater and pass it your bot's token.
updater = Updater("5178852679:AAEdjvFZ3j93WGZn0b8XwVyOM9_j9lxfHvI")

duration=10
counter=1
limitv=5
msgPass= 0
mediav=True
pic = None
promote="🎬Title: Spider-Man: No Way Home (2021) \n🎭Genre: Action/Adventure \n📀Quality: 1080p \n🔊Audio: English \n\n🔥Channel Link: https://t.me/+hWU_V7RyRyg2NzU1 \n❗️Post Link: https://t.me/c/1683386910/17"


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Up and Running, no problem")
    update.message.reply_text("Chat ID: "+str(update.effective_chat.id))

def spammoti(update: Update, context: CallbackContext):
    global counter
    while (counter<=limitv):
        if (pic != None):
            if(mediav==True):
                context.bot.send_photo(chat_id=update.effective_chat.id, photo=pic, caption=promote)
            else:
                update.message.reply_text(promote)
        else:
            update.message.reply_text(promote)
        counter+=1
        time.sleep(duration)
    counter=1
    update.message.reply_text("Limit touched!")

def media(update: Update, context: CallbackContext):
    global  mediav
    update.message.reply_text("Photo set to: "+str(mediav))
    update.message.reply_text("Tap /change to change")

def change(update: Update, context: CallbackContext):
    global mediav
    if (mediav==True):
        mediav=False
    else:
        mediav=True
    update.message.reply_text("Changed successfully to: "+str(mediav))

def timeMethod(update: Update, context: CallbackContext):
    update.message.reply_markdown_v2(fr'Enter the time interval:\-', reply_markup=ForceReply(selective=True))
    global msgPass
    msgPass=1
    updater.dispatcher.add_handler(MessageHandler(Filters.text, set))

def photo(update: Update, context: CallbackContext):
    update.message.reply_markdown_v2(fr'Upload the image with compression on:\-', reply_markup=ForceReply(selective=True))
    global msgPass
    msgPass=2
    updater.dispatcher.add_handler(MessageHandler(Filters.photo, set))

def clear(update: Update, context: CallbackContext):
    global pic
    pic = None
    update.message.reply_text("Photo deleted!")

def text(update: Update, context: CallbackContext):
    update.message.reply_markdown_v2(fr'Enter the text to be shown:\-',reply_markup=ForceReply(selective=True))
    global msgPass
    msgPass=3
    updater.dispatcher.add_handler(MessageHandler(Filters.text, set))

def limit(update: Update, context: CallbackContext):
    update.message.reply_markdown_v2(fr'Enter the limit:\-', reply_markup=ForceReply(selective=True))
    global msgPass
    msgPass = 4
    updater.dispatcher.add_handler(MessageHandler(Filters.text, set))

def set(update: Update, context: CallbackContext):
    global msgPass
    if(msgPass == 1):
        global duration
        try:
            duration = int(update.message.text)
            update.message.reply_text("Time interval set to: " + update.message.text + " seconds")
        except:
            update.message.reply_text("Enter a integer value!")
    if(msgPass == 2):
        global pic
        pic = update.message.photo[0].file_id
        try:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=pic, caption="Current Photo!")
            update.message.reply_text("Photo changed successfully! Press /clear to delete")
        except:
            update.message.reply_text("Error!")
    if (msgPass == 3):
        global promote
        promote = update.message.text
        update.message.reply_text("Text successfully updated to: \""+promote+"\"")
    if(msgPass==4):
        global limitv
        try:
            limitv = int(update.message.text)
            update.message.reply_text("Limit successfully set to "+str(limitv))
        except:
            update.message.reply_text("Enter a integer value!")
    msgPass=0

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Using this bot you can spam messages!  \n\nCommands:\n/start - Check whether bot is online \n/spammoti - Start the execution \n/time - Set the time interval (Default - 10 seconds) \n/photo - Set the picture to be shown \n/clear - Get some help \n/media - Set whether picture to be shown or not \n/text - Set the message to be shown or as the caption of the image \n/limit - Set how many messages to be sent (default - 5) \n/about - About Us")

def about(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_markdown_v2(fr'Hi {user.mention_markdown_v2()}\
This bot is created by [Adi ╰\_╯ Das](https://t.me/Adi5501)')

# on different commands - answer in Telegram
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("spammoti", spammoti))
updater.dispatcher.add_handler(CommandHandler("media", media))
updater.dispatcher.add_handler(CommandHandler("change", change))
updater.dispatcher.add_handler(CommandHandler("clear", clear))
updater.dispatcher.add_handler(CommandHandler("time", timeMethod))
updater.dispatcher.add_handler(CommandHandler("photo", photo))
updater.dispatcher.add_handler(CommandHandler("text", text))
updater.dispatcher.add_handler(CommandHandler("limit", limit))
updater.dispatcher.add_handler(CommandHandler("help", help))
updater.dispatcher.add_handler(CommandHandler("about", about))

updater.start_polling()
updater.idle()
