import os
import pickle
from address_book import AddressBook

FILE_NAME = "address_book.pkl"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)
FILE_PATH = os.path.join(DATA_DIR, FILE_NAME)


def save_data(book, filename=FILE_PATH):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename=FILE_PATH):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
