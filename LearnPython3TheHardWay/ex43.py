
# ex43 基本的面向对象分析和设计

from sys import exit
from random import randint
from textwrap import dedent


# 场景
class Scene(object):

    def enter(self):
        print("这是一个还没配置的房间")
        print("继承并实现它")


# 引擎
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


# 死亡场景
class Death(Scene):

    quips = [
        "你已死亡，你的很糟糕",
        "你妈妈以你为荣，如果他可以更聪明些",
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)


# 中央广场
class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        你遇到来自Percal25号行星的哥顿人，你要怎么做?
        - 1. 射击
        - 2. 躲开
        - 3. 讲个笑话
        """))

        action = input(">")

        if action == "射击" or action == "1":
            print("哥顿人武器比你先进，打死了你")
            return 'death'

        elif action == "躲开" or action == "2":
            print("哥顿人还是发现你，打死了你")
            return 'death'

        elif action == "讲个笑话" or action == "3":
            print("哥顿人成功被你逗笑，把你当做朋友")
            return 'laser_weapon_armory'

        else:
            print("无法识别")
            return 'central_corridor'


# 激光武器库
class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
        你需要密码才能解开武器库的大门，输入三位数密码:
        """))
        # code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        code = "123"
        guess = input("[keypad]>")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD")
            guesses += 1
            guess = input("[keypad]>")

        if guess == code:
            print("你打开了了武器库，你需要拿着激光武器去主控室开启")
            return 'the_bridge'

        else:
            print(dedent("""
            密码输入错误，引发了警报装置，你被警卫打死了
            """))
            return 'death'



# 主控室
class TheBridge(Scene):

    def enter(self):
        print(dedent("""
        你已进入主控室，你要做什么
        - 1. 扔下炸弹
        - 2. 轻放炸弹
        """))

        action = input(">")

        if action == "扔下炸弹" or action == "1":
            print(dedent("""
            炸弹碰撞，引发爆炸，你被炸死了
            """))
            return 'death'

        elif action == "轻放炸弹" or action == "2":
            print(dedent("""
            你成功开启炸弹倒计时
            """))
            return 'escape_pod'

        else:
            print("无法识别")
            return 'the_bridge'



# 逃生舱
class EscapePod(Scene):

    def enter(self):
        print(dedent("""
        你进入逃生舱,面前有五个按钮来启动飞船，启动失败会引发警报
        - 请输入1-5数字
        """))
        good_pod = randint(1, 5)
        guess = input("[pod #]>")

        if int(guess) != good_pod:
            print(dedent("""
            你选择错误，触发警报，被哥顿人打死了
            """))
            return 'death'
        else:
            print(dedent("""
            你启动成功了，逃生飞船起飞了
            """))
            return 'finished'


class Finished(Scene):
    def enter(self):
        print("你成功逃离哥顿人的魔掌！，干得漂亮")
        return 'finished'


# 地图
class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

