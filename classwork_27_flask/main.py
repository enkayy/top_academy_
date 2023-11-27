from flask import Flask
from datetime import datetime
import random



app = Flask(__name__)


@app.get("/")
def hello():
    return {"Hello": "World!!!"}, 201

# flask --app main run --reload --- reload команда, чтобы перезапускался сервер при изменениях
# insamnia или postman поставить, в инх можно сохранять (Запросы)


@app.get("/current-day")
def show_current_weekday():
    day = datetime.now().strftime("%A")
    return f"Today is {day}"


@app.get("/quote")
def show_random_quote():
    quotes = ["Плата за индивидуальность — одиночество.",
              "Громким смехом не скроешь дикой боли.",
              "Навсегда ничего не бывает."]
    quote = random.choice(quotes)
    return f"Цитата дня: {quote}"
