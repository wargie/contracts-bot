from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
)

# ---------- Reply-keyboards (поле ввода) ----------

def reply_start_kb() -> ReplyKeyboardMarkup:
    """Одна кнопка 'Старт' у поля ввода."""
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Старт")]],
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите «Старт»",
        selective=True,
    )

def reply_main_menu_kb() -> ReplyKeyboardMarkup:
    """Главное меню после нажатия 'Старт'."""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Запрос по ИНН")],
            [KeyboardButton(text="Договор")],
            [KeyboardButton(text="Выход")],
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие",
        selective=True,
    )

def reply_remove() -> ReplyKeyboardRemove:
    """Убрать клавиатуру."""
    return ReplyKeyboardRemove()

# ---------- Inline-keyboards (в сообщении) ----------

def choose_contract_type_kb() -> InlineKeyboardMarkup:
    # Пока один тип договора
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Договор оказания услуг", callback_data="type_services")]
    ])

def choose_output_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="DOCX", callback_data="out_docx"),
            InlineKeyboardButton(text="PDF", callback_data="out_pdf"),
            InlineKeyboardButton(text="Оба", callback_data="out_both"),
        ]
    ])

def confirm_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Сформировать", callback_data="confirm_yes")],
        [InlineKeyboardButton(text="Отмена", callback_data="confirm_no")],
    ])