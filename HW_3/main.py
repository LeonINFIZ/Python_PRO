from faker import Faker
import random
from flask import Flask, Response
import json
import pandas as pd
from webargs.flaskparser import use_kwargs
import time
import httpx

from count_of_students import count_of_students
from currency_and_convert import currency_and_convert

app = Flask(__name__)


@app.route("/generate_students")
@use_kwargs(
    count_of_students,
    location="query"
)
def generate_students(count_of_students):
    # count should be as input GET parameter
    # first_name, last_name, email, password, birthday (18-60)
    # save to csv and show on web page
    # set limit as 1000

    fake = Faker()
    students = {"Students": []}

    current_year = time.localtime().tm_year

    for i in range(count_of_students):
        # Берём строку день/месяц -> %d/%m и добавляем текущий год (current_year) - рандомное число от 18 до 60
        birthday = f"{fake.date(pattern='%d/%m')}/{current_year - random.randint(18, 60)}"

        students["Students"].append({"Name": fake.name(),
                                     "Last_Name": fake.last_name(),
                                     "Email": fake.email(),
                                     "Password": fake.password(),
                                     "Birthday": birthday})

    students_data = pd.DataFrame(students)
    students_data.to_csv("students.csv")

    return Response(json.dumps(students, indent=4), mimetype="application/json")


def show_it_beautifully(output_string: str, *, font_size_px=50, font_color="black"):
    """
    Функция возвращает передаваемый текст (output_string) в виде HTML разметки, отображенный по центру экрана,
    позволяется установить размер текста (font_size_px) и его цвет (font_color).
    """
    return (
        f'<div id="pass" style="font-size: {font_size_px}px; font-weight: bold; height: 100%; font-family: monospace;'
        f'display: flex; justify-content: center; align-items: center; color: {font_color}">{output_string}</div>\n')


@app.route("/bitcoin_rate")
@use_kwargs(
    currency_and_convert,
    location="query"
)
def get_bitcoin_value(currency, convert):
    # https://bitpay.com/api/rates
    # /bitcoin_rate?currency=UAH&convert=100
    # input parameter currency code
    # default is USD
    # default count is 1
    # return value currency of bitcoin
    # add one more input parameter count and multiply by currency (int)
    # * https://bitpay.com/api/
    # * Example: $, €, ₴
    # * return symbol of input currency code

    url = "https://bitpay.com/api/rates"
    result = httpx.get(url=url, params={})
    result = result.json()

    rate = 0

    # Получаем стоимость валюты
    for currency_item in result:
        if currency_item["code"] == f"{currency}":
            rate = currency_item["rate"]
            break
    else:
        return show_it_beautifully("ERROR: This currency does not exist", font_color="RED")

    answer = round(rate * convert, 2)

    # Получаем список валют
    url = "https://bitpay.com/currencies"
    result = httpx.get(url=url, params={})
    result = result.json()

    # Извлекаем символ
    symbol = ''
    for items in result["data"]:
        if items["code"] == f"{currency}":
            symbol = items["symbol"]

    # Извлекаем символ биткоина
    btc_symbol = result["data"][0]["symbol"]

    return show_it_beautifully(f"{convert}{btc_symbol} = {answer}{symbol}", font_color="GREEN")


if __name__ == "__main__":
    app.run(port=8000, debug=True)
