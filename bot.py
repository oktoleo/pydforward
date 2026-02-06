import os
import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from telegram.error import TelegramError

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Config sederhana
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# Rules: {source_chat_id: destination_chat_id}
FORWARD_RULES = {
    # Contoh: "-1001234567890": "-1000987654321"
    # Ganti dengan chat ID Anda
}

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    await update.message.reply_text(
        "🤖 **Telegram Forwarder Bot**\n\n"
        "Bot untuk forward pesan antar channel\n"
        "Cara pakai:\n"
        "1. Tambahkan bot ke channel sebagai admin\n"
        "2. Atur FORWARD_RULES di bot.py\n"
        "3. Bot akan auto forward semua pesan\n\n"
        "🔧 /help - Bantuan lengkap\n"
        "📊 /status - Status bot\n"
        "📍 /id - Dapatkan chat ID",
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    help_text = """
🆘 **BOT FORWARDER - BANTUAN**

📋 **CARA SETUP:**
1. Dapatkan chat ID channel:
   - Forward pesan ke @userinfobot
   - Atau gunakan /id command

2. Tambahkan ke FORWARD_RULES:
   ```python
   FORWARD_RULES = {
       "-1001234567890": "-1000987654321"
   }
