from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Создаем inline-клавиатуры
main = InlineKeyboardMarkup(
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
