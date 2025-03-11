import csv

import pandas as pd
from src.templates import read_csv, read_excel

def test_valid_csv_file(tmp_path):
    csv_path = tmp_path / "test.csv"
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Name', 'Age'])
        writer.writerow(['John', 25])
        writer.writerow(['Jane', 30])

    result = read_csv(str(csv_path))
    assert result[0]['Name'] == 'John'
    assert result[1]['Name'] == 'Jane'


def test_valid_excel_file(tmp_path):
    excel_path = tmp_path / "test.xlsx"
    df = pd.DataFrame({'Name': ['John', 'Jane'], 'Age': [25, 30]})
    df.to_excel(excel_path, index=False)

    result = read_excel(str(excel_path))
    assert result[0]['Name'] == 'John'
    assert result[1]['Name'] == 'Jane'


def test_invalid_file():
    assert read_excel("templates.xlsx") == []


def test_empty_excel_file(tmp_path):
    excel_path = tmp_path / "empty.xlsx"
    df = pd.DataFrame()
    df.to_excel(excel_path, index=False)

    result = read_excel(str(excel_path))
    assert result == []