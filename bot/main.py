import readline
from .contact_manager import ContactManager


def main():
    """Application entry point."""
    contact_manager = ContactManager()
    contact_manager.run()


if __name__ == "__main__":
    main()
