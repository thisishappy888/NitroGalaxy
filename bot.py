import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, LabeledPrice, PreCheckoutQuery

from dotenv import load_dotenv
import os

# Загрузка переменных из .env файла
load_dotenv()

bot_secret_key = os.getenv('BOT_SECRET_KEY')
bot = Bot(bot_secret_key)
dp = Dispatcher()

# Создаем inline-клавиатуры
main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Telegram Premium", callback_data="telegram_premium")],
        [InlineKeyboardButton(text="Discord Nitro", callback_data="discord_nitro")],
        [InlineKeyboardButton(text="Robux", callback_data="robux")],
        [InlineKeyboardButton(text="V-bucks", callback_data="vbucks")],
        [InlineKeyboardButton(text="Отзывы", callback_data="reviews")]
    ]
)

discord_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Basic", callback_data="nitro_basic")],
        [InlineKeyboardButton(text="Full", callback_data="nitro_full")],
    ]
)

nitro_full_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="На 3 месяца", callback_data="nitro_full_3_months")],
        [InlineKeyboardButton(text="На год", callback_data="nitro_full_1_year")],
    ]
)

nitro_basic_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="На 3 месяца", callback_data="nitro_basic_3_months")],
        [InlineKeyboardButton(text="На год", callback_data="nitro_basic_1_year")],
    ]
)

telegram_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="На 3 месяца", callback_data="premium_3_months")],
        [InlineKeyboardButton(text="На 6 месяцев", callback_data="premium_6_months")],
        [InlineKeyboardButton(text="На год", callback_data="premium_1_year")]
    ]
)

robux_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="500 Robux", callback_data="robux_500")],
        [InlineKeyboardButton(text="1000 Robux", callback_data="robux_1000")],
        [InlineKeyboardButton(text="2000 Robux", callback_data="robux_2000")],
        [InlineKeyboardButton(text="5250 Robux", callback_data="robux_5250")],
        [InlineKeyboardButton(text="11000 Robux", callback_data="robux_11000")],
        [InlineKeyboardButton(text="24000 Robux", callback_data="robux_24000")]
    ]
)

vbucks_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1000 V-bucks", callback_data="vbucks_1000")],
        [InlineKeyboardButton(text="2800 V-bucks", callback_data="vbucks_2800")],
        [InlineKeyboardButton(text="5000 V-bucks", callback_data="vbucks_5000")],
        [InlineKeyboardButton(text="13500 V-bucks", callback_data="vbucks_13500")],
    ]
)

# Обработчик команды /start
@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Выбери, что хочешь купить.", reply_markup=main_kb)

# Обработчик нажатий на inline-кнопки
@dp.callback_query(F.data == "telegram_premium")
async def telegram_premium_handler(callback: CallbackQuery):
    await callback.message.edit_text("Выберите, какой Telegram Premium вы хотите:", reply_markup=telegram_kb)

# Обработчик нажатий на inline-кнопки
@dp.callback_query(F.data == "discord_nitro")
async def telegram_premium_handler(callback: CallbackQuery):
    await callback.message.edit_text("Выберите, какой Discord Nitro вы хотите:", reply_markup=discord_kb)

# Обработчик нажатий на inline-кнопки
@dp.callback_query(F.data == "nitro_basic")
async def telegram_premium_handler(callback: CallbackQuery):
    await callback.message.edit_text("Выберите, какой Discord Nitro вы хотите:", reply_markup=nitro_basic_kb)

# Обработчик нажатий на inline-кнопки
@dp.callback_query(F.data == "nitro_full")
async def telegram_premium_handler(callback: CallbackQuery):
    await callback.message.edit_text("Выберите, какой Discord Nitro вы хотите:", reply_markup=nitro_full_kb)

# Обработчик нажатий на inline-кнопки
@dp.callback_query(F.data == "vbucks")
async def vbucks_handler(callback: CallbackQuery):
    await callback.message.edit_text("Выберите, сколько V-bucks вы хотите:", reply_markup=vbucks_kb)

@dp.callback_query(F.data == "robux")
async def robux_handler(callback: CallbackQuery):
    await callback.message.edit_text("Выберите, сколько Robux вы хотите:", reply_markup=robux_kb)

@dp.callback_query(F.data == "reviews")
async def reviews_handler(callback: CallbackQuery):
    await callback.message.edit_text("Отзывы: @thisishappy66")

# Обработчики покупок Telegram Premium
@dp.callback_query(F.data.startswith("premium_"))
async def premium_purchase(callback: CallbackQuery):
    if callback.data == "premium_3_months":
        title = "Telegram Premium на 3 месяца"
        amount = 2
    elif callback.data == "premium_6_months":
        title = "Telegram Premium на 6 месяцев"
        amount = 1000
    elif callback.data == "premium_1_year":
        title = "Telegram Premium на год"
        amount = 1500
    else:
        return

    await callback.message.answer_invoice(
        title=title,
        description="Приобретается в виде подарка на аккаунт, что является безопасным способом получения. Покупателю необходимо сообщить только @username получателя!",
        payload="access_to_private",
        currency="XTR",
        prices=[LabeledPrice(label="XTR", amount=amount)],
        photo_url="https://storage.yandexcloud.net/s3-metaratings-storage/images/8a/73/8a739405a40aeaf8cbd31f3582686305.png"
    )

# Обработчики покупок Discord Nitro Basic
@dp.callback_query(F.data.startswith("nitro_basic_"))
async def premium_purchase(callback: CallbackQuery):
    if callback.data == "nitro_basic_3_months":
        title = "Discord Nitro Basic на 3 месяца"
        amount = 500
    elif callback.data == "nitro_basic_1_year":
        title = "Discord Nitro Basic на год"
        amount = 750
    else:
        return

    await callback.message.answer_invoice(
        title=title,
        description="Discord Nitro – возможность общаться в Discord комфортнее! Используйте персонализированные эмодзи с серверов, установите анимированный аватар, наслаждайтесь эксклюзивными стикерами и бустите сервера с помощью бустов. У нас можно выбрать подписку на месяц или год. Discord Nitro – больше возможностей, больше удобства!",
        payload="access_to_private",
        currency="XTR",
        prices=[LabeledPrice(label="XTR", amount=amount)],
        photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTG-MrjzcAr3-869tSewLOCOvfU56Y3jlNQnw&s"
    )

# Обработчики покупок Discord Nitro Basic
@dp.callback_query(F.data.startswith("nitro_full_"))
async def premium_purchase(callback: CallbackQuery):
    if callback.data == "nitro_full_3_months":
        title = "Discord Nitro Full на 3 месяца"
        amount = 150
    elif callback.data == "nitro_full_1_year":
        title = "Discord Nitro Full на год"
        amount = 1200
    else:
        return

    await callback.message.answer_invoice(
        title=title,
        description="Discord Nitro – возможность общаться в Discord комфортнее! Используйте персонализированные эмодзи с серверов, установите анимированный аватар, наслаждайтесь эксклюзивными стикерами и бустите сервера с помощью бустов. У нас можно выбрать подписку на месяц или год. Discord Nitro – больше возможностей, больше удобства!",
        payload="access_to_private",
        currency="XTR",
        prices=[LabeledPrice(label="XTR", amount=amount)],
        photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTG-MrjzcAr3-869tSewLOCOvfU56Y3jlNQnw&s" 
    )

# Обработчики покупок Robux
@dp.callback_query(F.data.startswith("robux_"))
async def robux_purchase(callback: CallbackQuery):
    if callback.data == "robux_500":
        title = "500 Robux"
        amount = 200
    elif callback.data == "robux_1000":
        title = "1000 Robux"
        amount = 400
    elif callback.data == "robux_2000":
        title = "2000 Robux"
        amount = 900
    elif callback.data == "robux_5250":
        title = "5250 Robux"
        amount = 2300
    elif callback.data == "robux_11000":
        title = "11000 Robux"
        amount = 5000
    elif callback.data == "robux_24000":
        title = "24000 Robux"
        amount = 8500
    else:
        return

    await callback.message.answer_invoice(
        title=title,
        description="Крайне удобный способ доната! Получение происходит в виде кода активации, данные от аккаунта передавать не нужно! Специальный ваучер, представленный в цифровом варианте, с помощью которого можно пополнить внутриигровой счет на необходимое количество валюты.",
        payload="access_to_private",
        currency="XTR",
        prices=[LabeledPrice(label="XTR", amount=amount)],
        photo_url="https://img.tapimg.net/market/images/d27d248be10f2eda91fdf0e058c79d88.png"
    )


# Обработчики покупок V-bucks
@dp.callback_query(F.data.startswith("vbucks_"))
async def vbucks_purchase(callback: CallbackQuery):
    if callback.data == "vbucks_1000":
        title = "1000 V-bucks"
        amount = 450
    elif callback.data == "vbucks_2800":
        title = "2800 V-bucks"
        amount = 550
    elif callback.data == "vbucks_5000":
        title = "5000 V-bucks"
        amount = 1000
    elif callback.data == "vbucks_13500":
        title = "13500 V-bucks"
        amount = 2000
    else:
        return

    await callback.message.answer_invoice(
        title=title,
        description="Удобный и безопасный способ приобретения доната на ваш аккаунт! Покупка V-Bucks оформляется через Epic Games, отряды через Xbox. Для каждого приобретения необходима смена региона, которая входит в стоимость услуги!",
        payload="access_to_private",
        currency="XTR",
        prices=[LabeledPrice(label="XTR", amount=amount)],
        photo_url="https://cdn2.unrealengine.com/fortnite-vbucks-1200x1200-1200x1200-8050abc986bf.png"
    )


# Обработчик подтверждения оплаты
@dp.pre_checkout_query()
async def pre_checkout_query(event: PreCheckoutQuery):
    await event.answer(True)

# Обработчик успешной оплаты
@dp.message(F.successful_payment)
async def successful_payment(message: Message):
    await message.answer("Спасибо за покупку! Свяжитесь с @thisishappy66 для получения товара.")
    await bot.refund_star_payment(
        message.from_user.id, message.successful_payment.telegram_payment_charge_id
    )
    

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())