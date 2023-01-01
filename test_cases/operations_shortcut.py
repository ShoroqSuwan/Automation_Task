import csv
from pathlib import Path

datafile = 'input_data.csv'
cfgFileDirectory = 'data'
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(datafile)


def get_data():
    with open(DATA_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skipping the first row
        data = [row[0] for row in reader]

    return data
