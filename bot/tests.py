from .commands import add_contact, change_contact, show_phone, show_all
from .utils import parse_input
from .decorators import input_error
from .messages import MESSAGES
from .error_messages import ERROR_MESSAGES
from address_book import AddressBook, Record


def test_parse_input():
    assert parse_input("add John 12345") == ("add", ["John", "12345"])
    assert parse_input("   phone Alice  ") == ("phone", ["Alice"])
    assert parse_input("") == ("", [])
    assert parse_input("   ") == ("", [])


def test_add_contact():
    contacts = AddressBook()
    msg = add_contact(["John", "1234567890"], contacts)
    assert msg == MESSAGES["add_success"]
    contact = contacts.find("John")
    assert contact is not None
    assert any(phone.value == "1234567890" for phone in contact.phones)


def test_change_contact():
    contacts = AddressBook()
    contact = Record("John")
    contact.add_phone("1234567890")
    contacts.add_record(contact)

    msg = change_contact(["John", "1234567890", "0987654321"], contacts)
    assert msg == "🔄 Contact updated."
    updated_contact = contacts.find("John")
    assert any(p.value == "0987654321" for p in updated_contact.phones)
    assert not any(p.value == "1234567890" for p in updated_contact.phones)

    msg2 = change_contact(["Unknown", "000", "111"], contacts)
    assert msg2 == "❌ Contact not found."


def test_show_phone():
    contacts = AddressBook()
    contact = Record("Alice")
    contact.add_phone("1234567890")
    contacts.add_record(contact)

    assert "1234567890" in show_phone(["Alice"], contacts)
    assert "not found" in show_phone(["Bob"], contacts)


def test_show_all():
    contacts = AddressBook()
    a = Record("A")
    a.add_phone("1234567890")
    b = Record("B")
    b.add_phone("0987654321")
    contacts.add_record(a)
    contacts.add_record(b)

    result = show_all(contacts)
    assert "📇 Contact list:" in result
    assert "A" in result
    assert "B" in result

    empty_contacts = AddressBook()
    assert show_all(empty_contacts) == "📭 No contacts found."


@input_error
def trigger_key_error():
    raise KeyError


@input_error
def trigger_value_error():
    raise ValueError("Custom Error")


@input_error
def trigger_index_error():
    raise IndexError


@input_error
def trigger_type_error():
    raise TypeError


@input_error
def trigger_unexpected():
    raise RuntimeError("Something bad")


if __name__ == "__main__":
    test_parse_input()
    test_add_contact()
    test_change_contact()
    test_show_phone()
    test_show_all()

    assert trigger_key_error() == ERROR_MESSAGES["KeyError"]
    assert trigger_value_error() == ERROR_MESSAGES["ValueError"]("Custom Error")
    assert trigger_index_error() == ERROR_MESSAGES["IndexError"]
    assert trigger_type_error() == ERROR_MESSAGES["TypeError"]
    assert trigger_unexpected() == ERROR_MESSAGES["Unexpected"](
        RuntimeError("Something bad")
    )

    print("✅ All tests passed.")
