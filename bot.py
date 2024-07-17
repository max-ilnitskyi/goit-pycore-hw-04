def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    (name,) = args
    return contacts.get(name) or "Name not found"


def show_all(contacts):
    return "\n".join([" ".join(data) for data in contacts.items()])


def parse_input(raw_input: str):
    cmd, *args = raw_input.strip().casefold().split()
    cmd = cmd.strip().lower()
    return cmd, *args


EXIT_COMMANDS = {"exit", "close"}

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        command, *args = parse_input(input("enter text: "))

        if command == "hello":
            print("How can I help you?")
            continue

        if command == "add":
            print(add_contact(args, contacts))
            continue

        if command == "change":
            print(change_contact(args, contacts))
            continue

        if command == "phone":
            print(show_phone(args, contacts))
            continue

        if command == "all":
            print(show_all(contacts))
            continue

        if command in EXIT_COMMANDS:
            print("Good bye!")
            break

        print("Invalid command.")


if __name__ == "__main__":
    main()
