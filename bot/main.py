import readline
from .messages import MESSAGES
from .utils import parse_input
from .commands import (
    add_contact,
    add_birthday,
    show_all,
    show_birthday,
    show_help,
    show_phone,
    change_contact,
    birthdays,
)
from address_book import AddressBook


def main():
    contacts = AddressBook()
    print(MESSAGES["welcome"])

    while True:
        user_input = input(MESSAGES["prompt"])
        command, args = parse_input(user_input)

        if not command:
            continue

        if command in ["close", "exit"]:
            print(MESSAGES["goodbye"])
            break
        elif command == "hello":
            print(MESSAGES["greeting"])
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            print(birthdays(contacts))
        elif command in ["help", "-h"]:
            print(show_help())
        else:
            print(MESSAGES["invalid"])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(MESSAGES["goodbye"])
