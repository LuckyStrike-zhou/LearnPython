
# ex35 分支和函数

from sys import  exit


def gold_room():
    print("这是一个充满金子的房间，你准备拿走多少？")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("兄弟，尝试输入一个数字")

    if how_much < 50:
        print("很好，你并不贪婪，恭喜你获胜！")
        exit(0)
    else:
        dead("你太贪婪了！")


def bear_room():
    print("这里有只熊")
    print("熊有一大坨蜂蜜")
    print("胖熊在另一个房间前面")
    print("你想要怎么把熊移走？")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "拿走蜂蜜":
            dead("熊看见你了并且抓花了你的脸")
        elif choice == "嘲讽熊" and not bear_moved:
            print("熊从门前走开了")
            print("你现在可以穿过它了")
            bear_moved = True
        elif choice == "嘲讽熊" and bear_moved:
            dead("熊抓到你并打断了你的腿")
        elif choice == "打开门" and bear_moved:
            gold_room()
        else:
            print("你的意思我不明白🐻")


def cthulhu_room():
    print("现在你看到大魔头克鲁苏")
    print("你想逃命还是被吃掉？")

    choice = input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("好的， that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("你在一个黑暗的房间里")
    print("你左右各有一扇门")
    print("你要选择那扇门？")

    choice = input("> ")
    if choice == "左":
        bear_room()
    elif choice == "右":
        cthulhu_room()
    else:
        dead("你被困到死亡")


start()
