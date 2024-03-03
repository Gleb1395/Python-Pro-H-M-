import pprint
from http import HTTPStatus
from wsgiref import validate

import fake
import requests
from faker import Faker
from flask import Flask, request, Response
import string
import pandas as pd
import random
import webargs
from webargs import fields, validate
from webargs.flaskparser import use_kwargs
import httpx
import csv

app = Flask(__name__)


@app.route("/")
def hello_world():
    print(request.args.get('a'))
    return 'Hello'


@app.route("/generate-students")
@use_kwargs(
    {
        'number_of_people': fields.Int(
            missing=20,
            validate=[validate.Range(min_inclusive=True, max_inclusive=True, min=1, max=1000)]

        )
    },
    location='query'
)
def generate_students(number_of_people: int):
    fake_person = Faker()
    Faker.seed(0)
    dct_fake_person = dict()
    id: int = 1
    for _ in range(number_of_people):
        first_name = fake_person.first_name()
        last_name = fake_person.last_name()
        email_person = fake_person.ascii_email()
        password_person = fake_person.password()
        date_of_birth_person = fake_person.date_of_birth(None, minimum_age=18, maximum_age=60)
        dct_fake_person[id] = [first_name, last_name, email_person, password_person, date_of_birth_person]
        id += 1

    data = [{'id': key, 'first_name': value[0], 'last_name': value[1], 'email': value[2],
             'password': value[3], 'date_of_birth': value[4]} for key, value in dct_fake_person.items()]

    df = pd.DataFrame(data)
    df.set_index('id', inplace=True)
    df.to_csv('data.csv', index=True)
    html_table = df.to_html(table_id="example", classes="table table-striped table-bordered",
                            col_space=50, justify='center')
    return html_table


@app.route("/get-bitcoin-value")
@use_kwargs(
    {
        'currency': fields.Str(
            load_default='USD'
        ),
        'convert': fields.Int(
            load_default=1
        )
    },
    location='query'
)
def get_bitcoin_value(currency: str, convert: int):
    url = 'https://bitpay.com/api/rates'
    result = httpx.get(url)

    if result.status_code not in (HTTPStatus.MULTIPLE_CHOICES, HTTPStatus.OK, HTTPStatus.NOT_FOUND):
        return Response('ERROR: something went wrong', status=result.status_code)

    data: dict = result.json()
    converter = 0
    for currency_name in data:
        if currency_name.get('code') == currency:
            converter = float(currency_name.get('rate', 0)) * convert

    url = "https://test.bitpay.com/currencies"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "X-Accept-Version": "2.0.0"
    }
    symbol = ''

    response = requests.get(url, headers=headers).json()
    for item in response['data']:
        if item['code'] == currency:
            symbol = item['symbol']
    symbol_btc = response['data'][0]['symbol']

    return (f'{convert} {symbol_btc} <---->  BTC<br>'
            f'{converter} {symbol} <---->  {currency}')


if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )
pprint.pprint(get_bitcoin_value())
