from combolock import ComboLock

a = ComboLock(9, 25, 2)
a.turnRight(2)
a.turnLeft(3)
a.turnRight(3)
a.open()

a.reset()

a.turnRight(9)
a.turnLeft(24)
a.turnRight(17)
a.open()
# a.turn

