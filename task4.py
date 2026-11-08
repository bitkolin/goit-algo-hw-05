def input_error(func):
    """Декоратор: перехоплює помилки введення і повертає повідомлення."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
        except KeyError:
            return "Contact not found."

    return inner


def parse_input(user_input):
    """Розбиває введений рядок на команду (в нижньому регістрі) та аргументи."""
    parts = user_input.split()
    if not parts:                       # порожній ввід
        return "", []
    cmd, *args = parts
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    """Додає контакт: add [ім'я] [телефон]."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    """Змінює номер існуючого контакту: change [ім'я] [новий телефон]."""
    name, phone = args
    if name not in contacts:
        raise KeyError(name)  # навмисно викликаємо помилку, декоратор її зловить
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    """Повертає номер телефону контакту: phone [ім'я]."""
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts):
    """Повертає всі збережені контакти, кожен з нового рядка."""
    if not contacts:
        return "No contacts saved."
    lines = []
    for name, phone in contacts.items():
        lines.append(f"{name}: {phone}")
    return "\n".join(lines)


def main():
    """Головний цикл бота: читає команди і виводить відповіді."""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()