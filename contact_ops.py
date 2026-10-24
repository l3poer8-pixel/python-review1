from models import Contact


def add_contacts(contacts, name, phone_number, email):
    if find_contact(contacts, name) is not None:
        print("该联系人已存在")
        return
    contacts.append(Contact(name, phone_number, email))


def show_all(contacts):
    if not contacts:
        print("通讯录为空")
        return
    print("-----联系人列表-----")
    for i, p in enumerate(contacts, 1):
        print(f"{i}. {p.name}    {p.phone_number}    {p.email}")
    print(f"共 {len(contacts)} 位联系人")


def find_contact(contacts, search_name):
    for c in contacts:
        if c.name == search_name:
            return c
    return None


def search(contacts, search_name):
    if not contacts:
        print("通讯录为空，请添加联系人")
        return
    c = find_contact(contacts, search_name)
    if c is None:
        print("通讯录中不存在该联系人")
        return
    print(f"{c.name}    {c.phone_number}    {c.email}")


def change_information(contacts, search_name):
    c = find_contact(contacts, search_name)

    if c is None:
        print("通讯录中不存在该联系人")
        return

    print(f"当前信息：姓名={c.name}  电话={c.phone_number}  邮箱={c.email}")
    print("可修改的字段：name / phone_number / email")
    change_choose = input("请输入你要修改哪一项：")
    new_value = input("请输入新的内容：")

    if change_choose == "name":
        c.name = new_value
    elif change_choose == "phone_number":
        c.phone_number = new_value
    elif change_choose == "email":
        c.email = new_value
    else:
        print("不支持修改该项")
        return

    print("修改成功！")


def delete_information(contacts, search_name):
    c = find_contact(contacts, search_name)

    if c is None:
        print("通讯录中不存在该联系人")
        return

    contacts.remove(c)
    print("已删除")