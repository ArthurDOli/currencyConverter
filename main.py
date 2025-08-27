import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
api_key = os.getenv("API_KEY")

def convert(base_currency):
    currencies = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'
    response = requests.get(currencies)
    data = response.json()
    if data['result'] == 'success':
        return data
    else:
        print(f"API error! {data['error-type']}.")
        return None

def select_principal_currency():
    base_currency = input("Insert the base currency: ")
    data = convert(base_currency)
    return data

def get_amount():
    while True:
        try:
            amount_str = input("Insert the currency value: ")
            amount = float(amount_str)
            return amount
        except ValueError:
            print("Please, insert a valid numeric value.")

def select_secundary_currency():
    while True:
        data_principal = select_principal_currency()
        if data_principal is None:
            print('Unable to continue due to an API error.')
            print("Closing program.")
            break
        secundary_currency = input("Enter the currency you want to convert to: ")
        ammount_to_convert = get_amount()
        if secundary_currency in data_principal['conversion_rates']:
            conversion = data_principal['conversion_rates'][secundary_currency]
            print(f"1 {data_principal['base_code']} = {conversion} {secundary_currency}")
            converted_ammount = conversion * ammount_to_convert
            print(f"{int(ammount_to_convert)} {data_principal['base_code']} = {int(converted_ammount)} {secundary_currency}")
        else:
            print("Coin not found.")

        repeticao = input("Do you want to perform another conversion? (y/n)")
        if repeticao.lower != 'y':
            print("Closing program.")
            break

select_secundary_currency()