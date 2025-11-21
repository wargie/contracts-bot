# Contracts Bot (Telegram)

Телеграм-бот для составления договоров и проверки контрагентов по ИНН (DaData). Поддерживает генерацию DOCX/PDF, нумерацию договоров и реестр.

## Быстрый старт (Windows 11)

```powershell
git clone https://github.com/wargie/contracts-bot.git
cd contracts-bot

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

copy .env.example .env
# отредактируйте .env: TELEGRAM_BOT_TOKEN, DADATA_API_TOKEN

python -m app.main