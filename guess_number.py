import random
num = random.randint(1,100)
print("我想好了一个1-100的数字，你猜猜看。")
count=0
while True:
    guess =int(input("请输入你猜的数字:"))
    count+=1
    if guess > num:
        print("太大了")
    elif guess < num:
        print("太小了")
    else:
        print(f"恭喜你猜对了,用了{count}次")
        break
    if count==7:
        print(f"7次用完，答案是{num}")
        break