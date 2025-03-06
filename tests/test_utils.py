import json
import unittest
from unittest.mock import patch, mock_open
from src.utils import load_financial_transactions

class TestLoadFinancialTransactions(unittest.TestCase):

    @patch('src.utils.os.path.exists')
    def test_empty_file_path(self, mock_exists):
        mock_exists.return_value = False
        self.assertEqual(load_financial_transactions('nonexistent.json'), [])

    @patch('src.utils.os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_valid_json_file(self, mock_open, mock_exists):
        mock_exists.return_value = True
        with patch.object(json, 'load') as mock_load:
            mock_load.return_value = [{'transaction1': {}}, {'transaction2': {}}]
            self.assertEqual(load_financial_transactions('valid.json'), [{'transaction1': {}}, {'transaction2': {}}])

    @patch('src.utils.os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_invalid_json_file(self, mock_open, mock_exists):
        mock_exists.return_value = True
        with patch.object(json, 'load') as mock_load:
            mock_load.side_effect = json.JSONDecodeError('error', '', 0)
            self.assertEqual(load_financial_transactions('invalid.json'), [])

    @patch('src.utils.os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_not_list_data(self, mock_open, mock_exists):
        mock_exists.return_value = True
        with patch.object(json, 'load') as mock_load:
            mock_load.return_value = {'not_a_list': {}}
            self.assertEqual(load_financial_transactions('valid.json'), [])



if __name__ == '__main__':
    unittest.main()