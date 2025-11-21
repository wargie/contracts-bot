from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Главное меню (ReplyKeyboard)
def reply_main_menu_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [KeyboardButton(text="Запрос по ИНН"), KeyboardButton(text="Договор")],
            [KeyboardButton(text="Выход")],
        ],
    )


# Ниже — уже существующие inline-клавиатуры (оставляем)
def choose_contract_type_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Договор оказания услуг", callback_data="type_services")]
    ])


def choose_output_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="DOCX", callback_data="out_docx"),
         InlineKeyboardButton(text="PDF", callback_data="out_pdf"),
         InlineKeyboardButton(text="Оба", callback_data="out_both")]
    ])


def confirm_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Сформировать", callback_data="confirm_yes")],
        [InlineKeyboardButton(text="Отмена", callback_data="confirm_no")]
    ])