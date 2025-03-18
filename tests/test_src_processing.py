
import unittest
from src.processing import find_operations, count_operations_by_category
from src.processing import filter_by_state, sort_by_date
from tests.conftest import filter_by_state_open, filter_by_state_exit1, filter_by_state_exit2


def tests_filter_by_state1(filter_by_state_open, filter_by_state_exit1):
    assert filter_by_state(filter_by_state_open) == filter_by_state_exit1


def tests_filter_by_state2(filter_by_state_open, filter_by_state_exit2):
    assert filter_by_state(filter_by_state_open, "CANCELED") == filter_by_state_exit2


def tests_sort_by_date(sort_by_date_open, sort_by_date_exit):
    assert sort_by_date(sort_by_date_open) == sort_by_date_exit



class TestFindOperations(unittest.TestCase):



    def test_find_operations_no_matches(self):
        operations = [
            {'description': 'Операция 1'},
            {'description': 'Операция 2'}
        ]
        search_string = 'Нет совпадений'
        results = find_operations(operations, search_string)
        self.assertEqual(results, [])

    def test_find_operations_one_match(self):
        operations = [
            {'description': 'Операция 1'},
            {'description': 'Операция с поисковой строкой'}
        ]
        search_string = 'поисковой'
        results = find_operations(operations, search_string)
        self.assertEqual(len(results), 1)



class TestCountOperationsByCategory(unittest.TestCase):

    def test_count_operations_by_category_empty_list(self):
        operations = []
        categories = ['Категория 1', 'Категория 2']
        result = count_operations_by_category(operations, categories)
        self.assertEqual(result, {category: 0 for category in categories})

    def test_count_operations_by_category_no_matches(self):
        operations = [
            {'description': 'Операция 1'},
            {'description': 'Операция 2'}
        ]
        categories = ['Категория 1', 'Категория 2']
        result = count_operations_by_category(operations, categories)
        self.assertEqual(result, {category: 0 for category in categories})



if __name__ == '__main__':
    unittest.main()
