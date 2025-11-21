# Contracts Bot (Telegram)

Телеграм-бот для составления договоров и проверки контрагентов по ИНН (DaData). Поддерживает генерацию DOCX/PDF, нумерацию договоров и реестр.

## Требования
- Python 3.10+
- Токен Telegram Bot API (`TELEGRAM_BOT_TOKEN`)
- Токен DaData Suggestions (`DADATA_API_TOKEN`)

## Быстрый старт
```bash
git clone https://github.com/wargie/contracts-bot.git
cd contracts-bot

python -m venv .venv
source .venv/bin/activate  # для Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

cp .env.example .env
# заполните TELEGRAM_BOT_TOKEN и DADATA_API_TOKEN, при необходимости реквизиты OUR_*

python -m app.main
```

## Переменные окружения
- `TELEGRAM_BOT_TOKEN` — токен Telegram-бота (обязательно).
- `DADATA_API_TOKEN` — токен DaData для проверки контрагентов (обязательно).
- `OUR_*` — реквизиты вашей компании (ИНН/КПП, банк и т.д.); заполняются при необходимости или остаются значениями по умолчанию.
- `OUR_MANAGER_NAME`, `OUR_MANAGER_POST`, `OUR_ACTS_ON` — ФИО, должность и основание полномочий представителя.
