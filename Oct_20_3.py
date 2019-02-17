from random import randint

class Die():
    def __init__(self,sides):
        self.sides=sides

    def roll_die(self):
        print(randint(1,self.sides))

six=Die(6)
for vaule_6 in range(0,six.sides):
    six.roll_die()
print('---------')
ten=Die(10)
for vaule_10 in range(0,ten.sides):
    ten.roll_die()
print('---------')
twenty=Die(20)
for vaule_20 in range(0,ten.sides):
    twenty.roll_die()