import sys
import signal
from typing import Callable, Dict, Optional, List
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
from .persistence import load_data, save_data


class ContactManager:
    def __init__(self):
        self.address_book = load_data()
        self._setup_signal_handlers()
        self._initialize_commands()

    def _setup_signal_handlers(self) -> None:
        """Setup handlers for system signals."""
        signal.signal(signal.SIGINT, self._handle_shutdown)

    def _handle_shutdown(self, sig: int, frame) -> None:
        """Handle application shutdown gracefully."""
        self.save_and_exit()

    def _initialize_commands(self) -> None:
        """Initialize command handlers dictionary."""
        self.command_handlers: Dict[str, Callable] = {
            "add": self._wrap_handler(add_contact),
            "change": self._wrap_handler(change_contact),
            "phone": self._wrap_handler(show_phone),
            "add-birthday": self._wrap_handler(add_birthday),
            "show-birthday": self._wrap_handler(show_birthday),
            "birthdays": lambda _: birthdays(self.address_book),
            "all": lambda _: show_all(self.address_book),
            "help": lambda _: show_help(),
            "-h": lambda _: show_help(),
            "close": lambda _: self.save_and_exit(),
            "exit": lambda _: self.save_and_exit(),
            "hello": lambda _: say_hello(),
        }

    def _wrap_handler(self, handler: Callable) -> Callable:
        """Wrap command handlers to provide consistent interface."""
        return lambda args: handler(args, self.address_book)

    def save_and_exit(self) -> None:
        """Save data and exit the application."""
        save_data(self.address_book)
        say_goodbye()
        sys.exit(0)

    def process_command(self, command: str, args: List[str]) -> Optional[str]:
        """Process a single command with its arguments."""
        handler = self.command_handlers.get(command)
        if not handler:
            return MESSAGES["invalid"]
        return handler(args)

    def run(self) -> None:
        print(MESSAGES["welcome"])

        while True:
            try:
                user_input = input(MESSAGES["prompt"])
                command, args = parse_input(user_input)

                if not command:
                    continue

                if command in ("exit", "close"):
                    self.save_and_exit()
                    break

                result = self.process_command(command, args)
                if result:
                    print(result)

            except KeyboardInterrupt:
                self.save_and_exit()
            except Exception as e:
                print(f"An error occurred: {str(e)}")
