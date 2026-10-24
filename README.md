# Python 基础项目练习
学习 AI Agent 路线过程中的python练习集合，包含4个命令行小程序。

## 项目内容
guess_number.py :猜数字游戏（在1-100的范围内，最多七次）
calculator.py :四则运算计算器（支持连续计算，除零保护）
score_stats.py :成绩统计（总人数，总分，平均分，最高/最低，及格率）
main.py :命令行通讯录（增删查改 + JSON 持久化） 

# 运行环境
-Python 3.14
-无三方依赖，只用标准库

## 如何运行

通讯录: 
    
    python main.py

其他练习:
    
    python guess_number.py
    python calculator.py
    python score_stats.py

## 通讯录功能

1.添加联系人（姓名重复的时候拒绝重复添加）
2.查看全部联系人
3.按姓名查找
4.修改联系人的基本信息
5.删除联系人
6.数据自动保存,重启后仍然存在

## 项目结构
    
    python-review/
    |--main.py
    |--contact_ops.py
    |--storage.py
    |--contacts.json
    |--guess_number.py
    |--calcuator.py
    |--score_stats.py
    |--.gitignore

## 学到的内容
-Git版本管理与GitHub 推送
-虚拟环境（venv）与依赖管理(requirement.txt)
-Python 基础:变量、列表、字典、循环、函数
-函数返回值与模块拆分
-JSON数据持久化
-异常处理(FileNotFoundError,JSONDcodeError)
