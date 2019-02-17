class Restaurant():

    def __init__(self,name,type):
        self.name=name
        self.type=type
        self.number=0


    def describe(self):
        print('name: '+self.name+'\ntype: '+str(self.type))

    def open(self):
        print('restaurant is opening')

    def set_number(self,q):
        self.number=q

    def increment(self,w):
        self.number+=w


it=Restaurant('asshole',20)
it.describe()
it.open()
print('there is '+str(it.number)+' people')
it.number=12
print(it.number)
it.set_number(3)
print(it.number)
it.increment(7)
print(it.number)