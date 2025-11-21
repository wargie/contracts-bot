from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# --- Главное меню ---

def main_menu_kb() -> InlineKeyboardMarkup:
    """4 кнопки: Флексопринт, Флексограф, Докторпринт, Проверка по ИНН."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Флексопринт", callback_data="menu_flexoprint")],
        [InlineKeyboardButton(text="Флексограф", callback_data="menu_flexograph")],
        [InlineKeyboardButton(text="Докторпринт", callback_data="menu_doctorprint")],
        [InlineKeyboardButton(text="Проверка по ИНН", callback_data="menu_checkinn")],
    ])


# --- Меню условий оплаты для шаблонов компаний ---

def payment_menu_kb() -> InlineKeyboardMarkup:
    """3 кнопки: предоплата, отсрочка, 50/50."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Предоплата", callback_data="pay_prepay")],
        [InlineKeyboardButton(text="Отсрочка", callback_data="pay_delay")],
        [InlineKeyboardButton(text="50/50", callback_data="pay_5050")],
    ])


# --- Кнопки после отчёта по ИНН ---

def after_check_kb() -> InlineKeyboardMarkup:
    """Кнопки навигации после проверки ИНН."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="В главное меню", callback_data="check_home")],
        [InlineKeyboardButton(text="Новая проверка", callback_data="check_new")],
        [InlineKeyboardButton(text="Выход", callback_data="check_exit")],
    ])


# --- Старые клавиатуры (оставляем для генерации договора в текущем MVP) ---

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