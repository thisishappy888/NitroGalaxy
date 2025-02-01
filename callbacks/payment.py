from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery

from keyboards import inline

router = Router()

@router.callback_query(F.data == "telegram_premium")
async def telegram_premium_handler(callback: CallbackQuery):
    await callback.message.edit_text("Выберите, какой Telegram Premium вы хотите:", reply_markup=inline.telegram_kb)

# Обработчик нажатий на inline-кнопки
@router.callback_query(F.data == "discord_nitro")
async def telegram_premium_handler(callback: CallbackQuery):
    await callback.message.edit_text("Выберите, какой Discord Nitro вы хотите:", reply_markup=inline.discord_kb)

# Обработчик нажатий на inline-кнопки
@router.callback_query(F.data == "nitro_basic")
async def telegram_premium_handler(callback: CallbackQuery):
    await callback.message.edit_text("Выберите, какой Discord Nitro вы хотите:", reply_markup=inline.nitro_basic_kb)

# Обработчик нажатий на inline-кнопки
@router.callback_query(F.data == "nitro_full")
async def telegram_premium_handler(callback: CallbackQuery):
    await callback.message.edit_text("Выберите, какой Discord Nitro вы хотите:", reply_markup=inline.nitro_full_kb)

# Обработчик нажатий на inline-кнопки
@router.callback_query(F.data == "vbucks")
async def vbucks_handler(callback: CallbackQuery):
    await callback.message.edit_text("Выберите, сколько V-bucks вы хотите:", reply_markup=inline.vbucks_kb)

@router.callback_query(F.data == "robux")
async def robux_handler(callback: CallbackQuery):
    await callback.message.edit_text("Выберите, сколько Robux вы хотите:", reply_markup=inline.robux_kb)

@router.callback_query(F.data == "reviews")
async def reviews_handler(callback: CallbackQuery):
    await callback.message.edit_text("Отзывы: @thisishappy66")

# Обработчики покупок Telegram Premium
@router.callback_query(F.data.startswith("premium_"))
async def premium_purchase(callback: CallbackQuery):
    if callback.data == "premium_3_months":
        title = "Telegram Premium на 3 месяца"
        amount = 2
        payload="telegram_premium_3_months"
    elif callback.data == "premium_6_months":
        title = "Telegram Premium на 6 месяцев"
        amount = 1000
        payload="telegram_premium_9_months"
    elif callback.data == "premium_1_year":
        title = "Telegram Premium на год"
        amount = 1500
        payload="telegram_premium_1_year"
    else:
        return

    await callback.message.answer_invoice(
        title=title,
        description="Приобретается в виде подарка на аккаунт, что является безопасным способом получения. Покупателю необходимо сообщить только @username получателя!",
        payload=payload,
        currency="XTR",
        prices=[LabeledPrice(label="XTR", amount=amount)],
        photo_url="https://storage.yandexcloud.net/s3-metaratings-storage/images/8a/73/8a739405a40aeaf8cbd31f3582686305.png"
    )

# Обработчики покупок Discord Nitro Basic
@router.callback_query(F.data.startswith("nitro_basic_"))
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
@router.callback_query(F.data.startswith("nitro_full_"))
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
@router.callback_query(F.data.startswith("robux_"))
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
@router.callback_query(F.data.startswith("vbucks_"))
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
@router.pre_checkout_query()
async def pre_checkout_query(event: PreCheckoutQuery):
    await event.answer(True)

# Обработчик успешной оплаты
@router.message(F.successful_payment)
async def successful_payment(message: Message, bot: Bot):
    await message.answer("Спасибо за покупку! Свяжитесь с @thisishappy66 для получения товара.")
    await bot.refund_star_payment(
        message.from_user.id, message.successful_payment.telegram_payment_charge_id
    )

    payment_info = message.successful_payment
    # Получаем название товара из invoice_payload
    product_title = payment_info.invoice_payload  # Здесь вы можете указать название товара, которое хотите получить


    await bot.send_message(7773130966, f"Пользователь @{message.from_user.username} купил {product_title}")
    
