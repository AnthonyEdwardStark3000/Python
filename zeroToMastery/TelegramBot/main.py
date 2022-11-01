from telegram.ext import *
import config

print("The Bot is turning On .")

def start_command(update, context):
    update.message.reply_text("Hi \n Nice to meet you")

def help_command(update, context):
    update.message.reply_text("I am ready to help you, Just type anything to get the answers")

def custom_command(update, context):
    update.message.reply_text("Entered a custom command")

def handle_response(text: str):
    if "hello" in text:
        return "Hi"
    if "hey" in text:
        return "Hey what's up?"
    if "how are you" in text:
        return "I am fine, how about you"
    return "Sorry no idea."