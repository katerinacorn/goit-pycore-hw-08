from address_book import AddressBook, Record, Name, Phone

# Name
try:
    name = Name("Alice")
    assert name.value == "Alice"
except Exception:
    assert False, "Valid name should not raise error"

try:
    Name("")
    assert False, "Empty name should raise ValueError"
except ValueError:
    pass

# Phone
try:
    phone = Phone("1234567890")
    assert phone.value == "1234567890"
except Exception:
    assert False, "Valid phone should not raise error"

for invalid in ["123", "abc1234567", ""]:
    try:
        Phone(invalid)
        assert False, f"Invalid phone '{invalid}' should raise ValueError"
    except ValueError:
        pass

# Record
record = Record("Bob")
record.add_phone("1112223333")
record.add_phone("9998887777")
assert len(record.phones) == 2
assert record.find_phone("9998887777").value == "9998887777"

record.edit_phone("9998887777", "0000000000")
assert record.find_phone("0000000000") is not None

record.remove_phone("1112223333")
assert record.find_phone("1112223333") is None

# AddressBook
book = AddressBook()
book.add_record(record)

found = book.find("Bob")
assert found is record

book.delete("Bob")
assert book.find("Bob") is None

print("All tests passed.")
