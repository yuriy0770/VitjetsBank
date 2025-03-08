import json
import os
from typing import Dict
import requests
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")

with open("../data/operations.json", encoding="utf-8") as file:
    json_file = json.load(file)

filtered_json = [i for i in json_file if "state" in i and i["state"] == "EXECUTED"]


def func(transaction: Dict) -> float:
    """возвращает сумму транзакции"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]
    else:
        amount = transaction["operationAmount"]["amount"]
        value = transaction["operationAmount"]["currency"]["code"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={value}&amount={amount}"

        headers = {"apikey": "EdMpPSF3hlRPlRSr8Jb0uNsVE4emtYlR"}
        response = requests.request("GET", url, headers=headers)
        result = response.json()
        return result["result"]
