import unittest
from unittest.mock import patch, Mock
from src.external_api import func

class TestFunc(unittest.TestCase):

    @patch('src.external_api.requests.request')  # replace with actual module name
    def test_func_rub(self, mock_requests):
        transaction = {
            "operationAmount": {
                "currency": {"code": "RUB"},
                "amount": 1000.0
            }
        }
        result = func(transaction)
        self.assertEqual(result, 1000.0)

    @patch('src.external_api.requests.request')
    def test_func_usd_to_rub(self, mock_requests):
        transaction = {
            "operationAmount": {
                "currency": {"code": "USD"},
                "amount": 10.0
            }
        }
        mock_response = Mock()
        mock_response.json.return_value = {'result': 640.0}
        mock_requests.return_value = mock_response
        result = func(transaction)
        self.assertEqual(result, 640.0)

    @patch('src.external_api.requests.request')
    def test_func_eur_to_rub(self, mock_requests):
        transaction = {
            "operationAmount": {
                "currency": {"code": "EUR"},
                "amount": 10.0
            }
        }
        mock_response = Mock()
        mock_response.json.return_value = {'result': 720.0}
        mock_requests.return_value = mock_response
        result = func(transaction)
        self.assertEqual(result, 720.0)

    @patch('src.external_api.requests.request')
    def test_func_error(self, mock_requests):
        transaction = {
            "operationAmount": {
                "currency": {"code": "USD"},
                "amount": 10.0
            }
        }
        mock_response = Mock()
        mock_response.json.side_effect = Exception("API error")
        mock_requests.return_value = mock_response
        with self.assertRaises(Exception):
            func(transaction)

if __name__ == '__main__':
    unittest.main()