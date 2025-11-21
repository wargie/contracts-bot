# Бот «Составитель договоров» — MVP

## Установка и запуск
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env
python app/main.py
```

## Переменные окружения
- TELEGRAM_BOT_TOKEN — токен бота
- DADATA_API_TOKEN — токен DaData (верификация контрагентов)
- BOT_ADMINS — список id через запятую (опционально)

## Структура
См. каталог `app/` и комментарии в коде.