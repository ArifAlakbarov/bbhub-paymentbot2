import os
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
PUBLIC_CHANNEL = os.getenv("PUBLIC_CHANNEL", "https://t.me/bbhub18")
PRIVATE_CHANNEL = os.getenv("PRIVATE_CHANNEL", "https://t.me/+6PXbnF9xaNgzMzky")
LEOBANK_CARD = os.getenv("LEOBANK_CARD", "4098584496156348")
KAPITALBANK_CARD = os.getenv("KAPITALBANK_CARD", "5239151747840174")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer(f"Salam, xoş gəlmisiniz! Kanalımız: {PUBLIC_CHANNEL}\nÖdəniş üçün /pay yazın.")

@dp.message_handler(commands=["pay"])
async def pay_handler(message: types.Message):
    await message.answer(f"Ödəniş məlumatları:\nLeobank: {LEOBANK_CARD}\nKapitalbank: {KAPITALBANK_CARD}\nQəbzi göndərin.")

@dp.message_handler(commands=["tesdiq"])
async def confirm_payment(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return await message.reply("Siz admin deyilsiniz.")
    args = message.get_args()
    if args.isdigit():
        await bot.send_message(int(args), f"Təbriklər! Private kanal: {PRIVATE_CHANNEL}")
        await message.reply("İstifadəçiyə link göndərildi.")

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photo_handler(message: types.Message):
    await bot.send_message(ADMIN_ID, f"Yeni çek göndərildi:\n@{message.from_user.username}\nID: {message.from_user.id}")
    await bot.send_photo(ADMIN_ID, message.photo[-1].file_id)

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
