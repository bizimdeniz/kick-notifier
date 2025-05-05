FROM python:3.11-slim

WORKDIR /app

COPY app/ /app/

RUN pip install requests beautifulsoup4 python-telegram-bot

CMD ["python", "bot.py"]