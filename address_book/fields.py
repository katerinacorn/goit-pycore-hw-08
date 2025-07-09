class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str) or not new_value.strip():
            raise ValueError("Name cannot be empty")
        self._value = new_value.strip()


class Phone(Field):
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not new_value.isdigit() or len(new_value) != 10:
            raise ValueError("Phone number must be exactly 10 digits")
        self._value = new_value


from datetime import datetime, timedelta
from typing import Union

DATE_FORMAT = "%d.%m.%Y"


class Birthday(Field):
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        try:
            parsed_date = datetime.strptime(new_value, DATE_FORMAT)
            self._value = parsed_date
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self._value.strftime(DATE_FORMAT)
