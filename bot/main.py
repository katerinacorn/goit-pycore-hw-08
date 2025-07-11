import readline
import sys
import signal
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
    say_goodbye,
    say_hello,
)
from address_book import AddressBook
from .persistence import load_data, save_data

contacts = load_data()


def handle_sigint(sig, frame):
    save_data(contacts)
    say_goodbye()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_sigint)

COMMAND_HANDLERS = {
    "add": add_contact,
    "change": change_contact,
    "phone": show_phone,
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "birthdays": lambda _, contacts: birthdays(contacts),
    "all": lambda _, contacts: show_all(contacts),
    "help": lambda *_: show_help(),
    "-h": lambda *_: show_help(),
    "close": lambda *_: say_goodbye(),
    "exit": lambda *_: say_goodbye(),
    "hello": lambda *_: say_hello(),
}


def main():
    print(MESSAGES["welcome"])

    while True:
        user_input = input(MESSAGES["prompt"])
        command, args = parse_input(user_input)
        if not command:
            continue

        if command in ("exit", "close"):
            save_data(contacts)
            say_goodbye()
            break

        handler = COMMAND_HANDLERS.get(command)
        if not handler:
            print(MESSAGES["invalid"])
            continue

        result = handler(args, contacts) if callable(handler) else handler()
        if result:
            print(result)


if __name__ == "__main__":
    main()
