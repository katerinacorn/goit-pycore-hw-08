from collections import UserDict
from .record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

    def find(self, name: str) -> Record | None:
        return self.data.get(name)
    
    def get_upcoming_birthdays(self):
        upcoming = {}

        # TODO
            if record.birthday:
                bday_this_year = record.birthday.value.date().replace(year=today.year)

                if today <= bday_this_year <= next_week:
                    weekday = bday_this_year.strftime('%A')
                    if weekday in ['Saturday', 'Sunday']:
                        weekday = 'Monday'
                    upcoming.setdefault(weekday, []).append(record.name.value)

        return upcoming

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
