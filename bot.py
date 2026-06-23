import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8916412076:AAG39Q3YlI4lwogYPyFBLAWxdqPOSKHlgqw"
MINI_APP_URL = "https://poetic-dasik-b42ef5.netlify.app/resume.html"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("📄 CV Yaratish", web_app=WebAppInfo(url=MINI_APP_URL))
    ]])
    await update.message.reply_text(
        f"Salom, {update.effective_user.first_name}! 👋\n\n"
        "AI yordamida professional CV yasaymiz!\n\n"
        "✅ Ma'lumot kiriting\n"
        "✅ AI professional yozadi\n"
        "✅ PDF yuklab oling\n\n"
        "👇 Boshlash uchun tugmani bosing:",
        reply_markup=keyboard
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
