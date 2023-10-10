import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Cria uma instância do bot do Telegram
bot = telegram.Bot(token='6067341105:AAF_H8x9j8w6jhD5VVTSpAbKrIwQnWnGfXM')

# Função para enviar uma mensagem pré-pronta
def enviar_mensagem(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Olá! Como posso ajudar?')

# Função para responder "bom dia"
def responder_bom_dia(update, context):
    mensagem = update.message.text.lower()
    if "bom dia" in mensagem:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Olá, tudo bem, bom dia!')

# Cria uma instância do Updater e adiciona os handlers
updater = Updater(token='6067341105:AAF_H8x9j8w6jhD5VVTSpAbKrIwQnWnGfXM', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', enviar_mensagem))
dispatcher.add_handler(MessageHandler(filters.Text & ~filters.COMMAND, responder_bom_dia))

# Inicia o bot
updater.start_polling()
updater.idle()