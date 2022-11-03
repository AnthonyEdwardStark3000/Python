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


def handle_message(update, context):
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''
    print(f'User : {update.message.chat.id} said : {text} in {message_type}')

    if message_type == 'group':
        if '@AnthonyEdardStark' in text:
            new_text = text.replace('@AnthonyEdardStark', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)
    update.message.reply_text(response)


def error(update, context):
    print(f'Update {update} caused the error {context.error}')


if __name__ == '__main__':
    updater = Updater(config.token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling(1.0)
    updater.idle()
