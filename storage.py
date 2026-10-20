import json

FILE_NAME = "contacts.json"

def load_contacts():
    try:
        with open(FILE_NAME,"r",encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_contacts(contacts):
    with open(FILE_NAME, "w",encoding="utf-8") as f:
        json.dump(contacts,f,ensure_ascii=False,indent=2)
