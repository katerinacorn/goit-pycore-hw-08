from address_book import AddressBook, Record


def main():
    # Create a new address book
    book = AddressBook()

    # Create a record for John
    john = Record("John")
    john.add_phone("1234567890")
    john.add_phone("5555555555")
    book.add_record(john)

    # Create and add a record for Jane
    jane = Record("Jane")
    jane.add_phone("9876543210")
    book.add_record(jane)

    # Print all records in the book
    print("\n📒 Address Book contents:")
    for name, record in book.data.items():
        print(record)

    # Find and edit a phone number for John
    print("\n✏️ Editing John's phone number:")
    john.edit_phone("1234567890", "1112223333")
    print(john)

    # Search for a phone number in John's record
    print("\n🔍 Searching for a phone number in John's record:")
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    # Delete Jane's record
    print("\n🗑️ Deleting Jane's record...")
    book.delete("Jane")

    # Final contents of the book
    print("\n📒 Final Address Book contents:")
    for name, record in book.data.items():
        print(record)

    # Print the book object directly
    print("\n📒 Address Book object:")
    print(book)


if __name__ == "__main__":
    main()
