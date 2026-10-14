while True:
    num1=float(input("请输入第一个数字:"))
    op=input("请输入运算符(+,-,*,/):")
    num2=float(input("请输入第二个数字:"))
    if op=="+":
        print("目前计算器模式是加法")
        print(f"结果:{num1}+{num2} = {num1+num2}")
    elif op=="-":
        print("目前计算器模式是减法")
        print(f"结果:{num1}-{num2} = {num1-num2}")
    elif op=="*":
        print("目前计算器模式是乘法")
        print(f"结果是:{num1}*{num2} = {num1*num2}")
    elif op=="/":
        print("目前计算器模式是除法")
        if num2==0:
            print("错误:不能除以0")
        else:
            print(f"结果是:{num1}/{num2} = {num1/num2}")
    print("还要继续吗？(y/n):")
    choose=input()
    if choose=="n":
        print("计算机已退出")
        break
    else:
        print("不支持的运算符")