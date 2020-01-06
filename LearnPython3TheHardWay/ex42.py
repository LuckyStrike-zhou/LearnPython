
# ex42对象、类以及从属关系


class Animal(object):
    pass


class Dog(Animal):

    def __init__(self, name):

        self.name = name


class Cat(Animal):

    def __init__(self, name):
        self.name = name


class Person(Animal):

    def __init__(self, name):
        self.name = name
        self.pet = None # 人有那种宠物


# 职员，工资
class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)

        self.salary = salary


class Fish(object):
    pass


# 鲑鱼
class Salmon(Fish):
    pass


# 大比目鱼
class Halibut(Fish):
    pass


rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 12000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()


