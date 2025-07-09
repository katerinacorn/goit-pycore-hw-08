from collections import UserDict
from .record import Record

from datetime import date, datetime, timedelta
from typing import List, Dict

DATE_FORMAT = "%d.%m.%Y"
DAYS_IN_WEEK = 7
SATURDAY = 5
SUNDAY = 6
WEEKEND_DAYS = (SATURDAY, SUNDAY)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

    def find(self, name: str) -> Record | None:
        return self.data.get(name)

    def get_upcoming_birthdays(self) -> List[Dict[str, str]]:
        today = datetime.today().date()
        users_to_congratulate = []

        for user in self.data.values():
            if not isinstance(user, Record):
                continue

            if not user.birthday:
                continue

            name = user.name.value
            birthday_date = user.birthday.value

            try:
                birthday_date_this_year = birthday_date.replace(year=today.year)

                congratulation_date = self._get_congratulation_date(
                    birthday_date_this_year
                )
                days_to_congratulation = (congratulation_date - today).days

                if not 0 <= days_to_congratulation <= DAYS_IN_WEEK:
                    continue

                user_dict = {
                    "name": name,
                    "congratulation_date": congratulation_date.strftime(DATE_FORMAT),
                }
                users_to_congratulate.append(user_dict)
            except ValueError:
                print("Incorrect date format: expected 'DD.MM.YYYY' format.")
                continue

        return users_to_congratulate

    def _get_congratulation_date(self, birthday_date: date) -> date:
        weekday = birthday_date.weekday()

        if weekday in WEEKEND_DAYS:
            days_to_monday = timedelta(DAYS_IN_WEEK - weekday)
            return birthday_date + days_to_monday

        return birthday_date

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
