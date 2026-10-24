import json
from models import Contact

FILE_NAME = "contacts.json"


def load_contacts():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

    contacts = []
    for d in data:
        contacts.append(Contact(d["name"], d["phone_number"], d["email"]))
    return contacts


def save_contacts(contacts):
    data = []
    for c in contacts:
        data.append(c.to_dict())

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
