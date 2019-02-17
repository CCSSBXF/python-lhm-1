class Employee():
    def __init__(self,first,last,money):
        self.first=first
        self.last=last
        self.money=money

    def give_raise(self,increase):
        if increase:
            self.money+=int(increase)
        else:
            self.money+=5000