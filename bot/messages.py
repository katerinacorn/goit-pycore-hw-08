MESSAGES = {
    "welcome": "👋🤖 Welcome to the assistant bot!",
    "prompt": "👉 Enter a command: ",
    "goodbye": "\n👋🤖 Good bye!",
    "greeting": "🖐️ How can I help you?",
    "invalid": "❓ Invalid command.",
    "add_success": "✅ Contact added.",
    "change_success": "🔄 Contact updated.",
    "phone_found": lambda name, phone: f"📞 {name}'s phone number is {phone}",
    "contact_not_found": "❌ Contact not found.",
    "all_empty": "📭 No contacts found.",
    "all_header": "📇 Contact list:",
    "all_entry": lambda entry: f"\t 📌 {str(entry)}",
    "birthday_added": "🎉 Birthday added successfully.",
    "birthday_found": lambda name, birthday: f"🎂 {name}'s birthday is {birthday}",
    "birthday_not_found": lambda name: f"{name} has no birthday information.",
    "help": (
        "📖 Available commands:\n"
        "  hello                  - Greet the bot\n"
        "  add <name> <phone>     - Add a new contact\n"
        "  change <name> <phone>  - Update existing contact\n"
        "  phone <name>           - Show contact's phone number\n"
        "  add-birthday \n "
        "  <name> <DD.MM.YYYY>    - Add contact's birthday\n"
        "  show-birthday <name>   - Show contact's birthday\n"
        "  birthdays              - Shaw all birthdays\n"
        "  all                    - Show all contacts\n"
        "  help or -h             - Show this help message\n"
        "  close or exit          - Exit the assistant\n"
    ),
}
