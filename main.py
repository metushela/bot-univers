import telebot
import json
import os
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "7980302462:AAFS3EBrr1qaeWVwsY63W_fusboMlNKETE8"  # ← Mets ton vrai token ici
bot = telebot.TeleBot(BOT_TOKEN)

DATA_FILE = "qcm_data.json"
états_utilisateur = {}

# Charger les questions
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        qcm_data = json.load(f)
else:
    qcm_data = []

# 📌 /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 Bienvenue !\n- /ajouter pour ajouter une question\n- /liste pour voir les questions\n- /quiz pour lancer un QCM.")

# 📝 /ajouter
@bot.message_handler(commands=['ajouter'])
def ajouter(message):
    bot.send_message(message.chat.id, "📝 Envoie la **question**.")
    états_utilisateur[message.chat.id] = {"étape": "question"}

# 📋 /liste
@bot.message_handler(commands=['liste'])
def liste(message):
    if not qcm_data:
        bot.send_message(message.chat.id, "Aucune question enregistrée.")
    else:
