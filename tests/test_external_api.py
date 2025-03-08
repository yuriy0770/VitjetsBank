import os
import unittest
from unittest.mock import patch
import json
from dotenv import load_dotenv
from src.external_api import func

load_dotenv("template.env")
API_KEY = os.getenv('API_KEY')

class TestFunc(unittest.TestCase):




    @patch('requests.request')
    def test_api_call(self, mock_request):
        with open("data/operations.json", encoding="utf-8") as file:
            json_file = json.load(file)

        transaction = {'operationAmount': {'currency': {'code': 'USD'}, 'amount': 100}}
        result = func(transaction)
        mock_request.assert_called_once_with('GET', "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100",
                                                headers={'apikey': API_KEY})



if __name__ == '__main__':
    unittest.main()