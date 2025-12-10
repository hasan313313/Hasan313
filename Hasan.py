import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# اسم البوت العادي
BOT_NAME = "حسن"

# جمل الرد
RESPONSES = [
    "نعم حبي؟",
    "تدلّل شتريد؟",
    "عيوني مصطفى ❤️",
    "هااا شكو؟",
    "تفضل آني هنا.",
    "هلاا شتحتاج؟",
    "يمك دوم، احجي.",
    "أسمعك، كلمني.",
    "هلا والله بالمصطفى.",
    "أكو شي؟"
]

async def reply_on_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # التحقق من وجود اسم البوت في الرسالة
    if BOT_NAME in text:
        response = random.choice(RESPONSES)
        await update.message.reply_text(response)

async def main():
    token = os.getenv("BOT_TOKEN")  # لا تضع التوكن هنا — ضعه في Render
    app = ApplicationBuilder().token(token).build()

    # التقاط جميع النصوص
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_on_name))

    print("BOT RUNNING...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
