
# ex44 继承与组合


# 隐式继承

class Parent(object):

    def implicit(self):
        print("Parent implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    # pass
    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()