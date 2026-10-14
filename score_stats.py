def average(score):
    average_score=sum(score)/len(score)
    return average_score
def judge_score():
    num=0
    for x in score:
        if x >= 60:
            num+=1
    return num
def precent_score_of_pass():
    precent=judge_score()/len(score)
    return precent
line=input("请输入几个数字（用空格隔开）：")
parts=line.split()
score=[]
for x in parts:
    score.append(float(x))
print("=====成绩统计=====")
print("总人数:",len(score))
print("总分:",int(sum(score)))
print(f"平均分:{average(score):.2f}")
print("最高分:",max(score))
print("最低分:",min(score))
print("及格人数:",judge_score())
print(f"及格率:{precent_score_of_pass():.1%}")
