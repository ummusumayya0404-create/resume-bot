import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = "8916412076:AAG39Q3YlI4lwogYPyFBLAWxdqPOSKHlgqw"
MINI_APP_URL = "https://poetic-dasik-b42ef5.netlify.app/resume.html"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name or "Foydalanuvchi"
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("📄 CV Yaratish", web_app=WebAppInfo(url=MINI_APP_URL))
    ]])
    await update.message.reply_text(
        f"Salom, {name}! 👋\n\n"
        "Men AI yordamida professional CV/Resume yasaydigan botman.\n\n"
        "✅ Ma'lumotlaringizni kiriting\n"
        "✅ AI professional tarzda yozadi\n"
        "✅ PDF ko'rinishida yuklab oling\n\n"
        "Pastdagi tugmani bosing va boshlang! 👇",
        reply_markup=keyboard
    )

async def cv_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("📄 CV Yaratish", web_app=WebAppInfo(url=MINI_APP_URL))
    ]])
    await update.message.reply_text("CV yaratishni boshlash uchun:", reply_markup=keyboard)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cv", cv_command))
    logger.info("Bot ishga tushdi...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
