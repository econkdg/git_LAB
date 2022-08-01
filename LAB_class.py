# ====================================================================================================
# class 1
# ====================================================================================================
# class: set of member & method

# member: variable
# method: function
# object -> instance (by class)

class car:

    # constructor
    def __init__(self, name, color):
        self.name = name  # member 1
        self.color = color  # member 2

    # class mothod
    def show_info(self):
        print("name:", self.name, "/color:", self.color)

    # setter method
    def set_name(self, name):
        self.name = name

    # destructor
    def __del__(self):
        print("destruct instance!")


car1 = car("hyundai", "red")
car1.show_info()

car2 = car("ford", "black")
car2.show_info()

car1.set_name("mersedes-benz")

del car1
# ----------------------------------------------------------------------------------------------------
# inheritance

# super class
# sub class


class UNIT:

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(self.name, "attack the monster!. [power:", self.power, "]")


unit = UNIT("unit 1", 375)
unit.attack()


class MONSTER(UNIT):

    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type


monster = MONSTER("monster1", 10, "basic")

monster.attack()
# ----------------------------------------------------------------------------------------------------
# reference

# https://www.youtube.com/watch?v=YQhJsWj6ydU
# ====================================================================================================
