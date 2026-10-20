from storage import load_contacts, save_contacts
from contact_ops import add_contacts, show_all, search, change_information, delete_information

def main():
    contacts=load_contacts()

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

if __name__ == "__main__":
    main()