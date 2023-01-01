import pytest
from pages.google_page import google_result
from pages.yahoo_page import yahoo_result
from pages.bing_page import bing_result
from test_cases.operations_shortcut import get_data
import csv
from pathlib import Path

datafile = 'input_data.csv'
cfgFileDirectory = 'data'
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(datafile)

insert = []


@pytest.mark.parametrize("data", get_data())
def test_run(data):
    insert.append([data, google_result(data), yahoo_result(data), bing_result(data)])

    with open(BASE_DIR.joinpath(cfgFileDirectory).joinpath('search_output.csv'), 'w', newline='',
              encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['search text', 'Google result', 'yahoo result', 'Bing result'])
        csv_writer.writerows(insert)
        csvfile.close()
