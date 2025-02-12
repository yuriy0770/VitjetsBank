import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import filter_by_state_open, filter_by_state_exit1, filter_by_state_exit2


def tests_filter_by_state1(filter_by_state_open, filter_by_state_exit1):
    assert filter_by_state(filter_by_state_open) == filter_by_state_exit1

def tests_filter_by_state2(filter_by_state_open, filter_by_state_exit2):
    assert filter_by_state(filter_by_state_open, 'CANCELED') == filter_by_state_exit2


def tests_sort_by_date(sort_by_date_open, sort_by_date_exit):
    assert sort_by_date(sort_by_date_open) == sort_by_date_exit