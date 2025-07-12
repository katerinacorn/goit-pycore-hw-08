import os
import pickle
from address_book import AddressBook

FILE_NAME = "address_book.pkl"
DATA_DIR = "data"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR_PATH = os.path.join(BASE_DIR, DATA_DIR)

os.makedirs(DATA_DIR_PATH, exist_ok=True)
FILE_PATH = os.path.join(DATA_DIR_PATH, FILE_NAME)


def save_data(book, filename=FILE_PATH):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename=FILE_PATH):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
