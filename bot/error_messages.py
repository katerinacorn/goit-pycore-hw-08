ERROR_MESSAGES = {
    "KeyError": "Unknown key. Please check the command.",
    "ValueError": lambda e: f"Invalid input. {str(e)}",
    "IndexError": "Missing arguments. Please provide the required information.",
    "TypeError": "Invalid argument type or count.",
    "Unexpected": lambda e: f"😱 Unexpected error: {str(e)}",
}