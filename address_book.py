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
    with open(FILE_NAME,"w",encoding="utf-8") as f:
        json.dump(contacts,f,ensure_ascii=False,indent=2)

contacts=load_contacts()

def add_contacts(contacts,name,phone_number,email):
    if find_contact(contacts,name) is not None:
        print("该联系人已存在")
        return
    contacts.append({"name":name,"phone_number":phone_number,"email":email})

def show_all(contacts):
    if not contacts:
        print("通讯录为空")
        return
    print("-----联系人列表-----")
    for i,p in enumerate(contacts,1):
        print(f"{i}.{p['name']} {p['phone_number']} {p['email']}")
    print(f"共{len(contacts)}位联系人")

def find_contact(contacts,search_name):
    for i in contacts:
        if i['name']==search_name:
            return i
    return None

def search(contacts,search_name):
    if not contacts:
        print("通讯录为空，请添加联系人")
        return
    i = find_contact(contacts,search_name)
    if i is None:
        print("通讯录中不存在该联系人")
        return
    else:
        print(f"{i['name']} {i['phone_number']} {i['email']}")

def change_information(contacts, search_name):
        i = find_contact(contacts, search_name)

        if i is None:
            print("通讯录中不存在该联系人")
            return

        print(f"当前信息：姓名={i['name']}  电话={i['phone_number']}  邮箱={i['email']}")
        print("可修改的字段：name / phone_number / email")
        change_choose = input("请输入你要修改哪一项：")
        new_value = input("请输入新的内容：")

        if change_choose == "name":
            i["name"] = new_value
        elif change_choose == "phone_number":
            i["phone_number"] = new_value
        elif change_choose == "email":
            i["email"] = new_value
        else:
            print("不支持修改该项")
            return

        print("修改成功！")

def delete_information(contacts, search_name):
        i = find_contact(contacts, search_name)

        if i is None:
            print("通讯录中不存在该联系人")
            return

        contacts.remove(i)
        print("已删除")


while True:
    print("=====通讯录=====")
    print("1.添加联系人")
    print("2.查看全部")
    print("3.查找联系人")
    print("4.修改联系人")
    print("5.删除联系人")
    print("0.退出")
    choose=input("请选择:")
    if choose=="1":
        name=input("请输入姓名:")
        phone_number=input("请输入电话:")
        email=input("请输入邮箱:")
        add_contacts(contacts,name,phone_number,email)
        save_contacts(contacts)
    elif choose=="2":
        show_all(contacts)
    elif choose=="3":
        search_name=input("请输入你要查找的人名:")
        search(contacts,search_name)
    elif choose=="4":
        search_name = input("请输入要修改的人名：")
        change_information(contacts, search_name)
        save_contacts(contacts)
    elif choose=="5":
        search_name = input("请输入要删除的人名：")
        delete_information(contacts, search_name)
        save_contacts(contacts)
    elif choose=="0":
        print("程序已退出")
        break
    else:
        print("暂不支持该选项")