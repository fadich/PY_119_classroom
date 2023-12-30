import json
import logging

contact = {
    "phone_number": "+38067456123",
    "first_name": "Gandalf",
    "last_name": "The Grey",
    "city": "Gondor",
    "state": "Middleearth",
}
contacts = {
    "+38067456123": {
        "phone_number": "+38067456123",
        "first_name": "Gandalf",
        "last_name": "The Grey",
        "city": "Gondor",
        "state": "Middleearth",
    },
}

# ========= contacts/database.py =========


def add_contact(contact: dict):
    key = contact["phone_number"]
    contacts[key] = contact


def delete_contact(phone_number: str):
    del contacts[phone_number]


def save(path: str):
    with open(path, "w") as file:
        file.write(json.dumps(contacts))
        # json.dump(
        #     obj=contacts,
        #     fp=file,
        # )


# ========= contacts/iu.py ==========


def read_phone_number():
    # while True:
    phone_number = input("phone_number: ")
    # ... validation

    return phone_number


def read_first_name():
    first_name = input("first_name: ")
    # ... validation

    return first_name


def read_contact():
    return {
        "phone_number": read_phone_number(),
        "first_name": read_first_name(),
        # "last_name": "The Grey",
        # "city": "Gondor",
        # "state": "Middleearth",
    }


# ========= main.py =========


def read_operation():
    operation = input(">>> ")
    # ... validation

    return operation


def read_filepath():
    path = input("Contact filepath: ")
    # ... validation

    return path


def add_handler(filepath: str):
    contact = read_contact()
    add_contact(contact)
    save(filepath)
    print("Contact added successfully")


def main():
    filepath = read_filepath()
    while True:
        print("<INSTRUCTION FOR USERS>")

        operation = read_operation()

        if operation in ("a", "add", "add_contact"):
            add_handler(filepath)
        elif operation in ():
            ...
        elif operation in ("e", "exit"):
            break
        else:
            print(f"!!! Invalid operation `{operation}` !!!")


if __name__ == "__main__":
    main()
