# print("Hello World!")
# 输入
# subject = input("主语: ")
# verb = input("谓语: ")
# object = input("宾语: ")
# print("%s %s %s" % (subject, verb, object))

# i = 0
# while i < 4:
#     i += 1 #这里也可以用 i = i + 1 ，但没有 i++ 这样的语法糖
#     print("*********")
#
# for i in range(4):
#     for j in range(2 * i + 1):
#         print("*", end="")  # 输出一个星号，但不换行
#     print()  # 输出一个换行
#
# for i in range(4):
#     print("*" * (2 * i + 1)) # Python 的字符串乘法会将字符串重复 n 次
#
# for i in range(4):
#     if i in [0, 3]:
#         print("*********")
#     else:
#         print("*       *")

# maze = [
#     'IXX.XO',
#     '..X.X.',
#     'X.X...',
#     '....X.',
#     '.XX..X',
# ]
#
#
# def findElement(maze, element):  # 定义一个函数，接受两个参数
#     for i in range(len(maze)):
#         for j in range(len(maze[i])):
#             if maze[i][j] == element:
#                 return [i, j]
#     raise Exception("迷宫中找不到" + element)
#
#
# entry = findElement(maze, 'I')
#
#
# exit_diy = findElement(maze, 'O')
#
#
# print('entry is', entry)
# print('exit is', exit_diy)

# import time
#
#
# def gettime(func):
#     """统计函数运行时间"""
#     #  接收所有 位置参数 关键字参数
#     def inner(*args, **kwargs):
#         begin = time.time()
#         #   接收所有 位置参数 关键字参数 -- 原封不动 传送给func
#         # 在调用完成 被修改的函数的功能之后 暂时保存返回值 待整体完成后返回
#         ret = func(*args, **kwargs)
#         end = time.time()
#         print("函数运行所需的时间是 %f秒" % (end-begin))
#         return ret
#     return inner
#
# @gettime
# def f1(number):
#     print("in f1 %d" % number)
#     for i in range(2):
#         time.sleep(1)
#
#     return 520
#
# @gettime
# def run(number1, number2):
#     time.sleep(1)
#     print("in run %d" % (number1 + number2))
#     return 131410086
# print(f1(100))
# print(run(1,999))
s = input("请输入：")
print(s)
print(type(s))
print("你输入的内容是:", print(s))
print(s)
a = [x*5 for x in range(2,10,2)]
print(a)
