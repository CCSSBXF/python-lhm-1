class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0

    def get(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print(str(self.odometer)+' mile in it')

    def updata_odometer(self,mileage):
        if mileage>=self.odometer:
            self.odometer=mileage
        else:
            print('can not roll back')

    def increment_odometer(self,miles):
        self.odometer+=miles

new_car=Car('aude','a4',2016)
print(new_car.get())
new_car.odometer=24
new_car.read_odometer()

new_car.updata_odometer(12)
new_car.read_odometer()

new_car.increment_odometer(20)
new_car.read_odometer()
print('\n*****************************************\n')

class Battery():
    def __init__(self,bsize=32):
        self.bsize=bsize

    def describe_b(self):
        print('this car has '+str(self.bsize)+'kwn')

    def get_range(self):
        range=self.bsize*10
        message='this car can go '+str(range)
        message+='mile '
        print(message)

    def upgrade(self):
        self.bsize=85

class ElectricCar(Car):
    """继承"""
    def __init__(self,make,model,year):
        '''初始化父类属性,加上特有的'''
        super().__init__(make,model,year)
        self.bsize=Battery()

my_tesla=ElectricCar('tesla','S',2018)
print(my_tesla.get())
my_tesla.bsize.describe_b()
my_tesla.bsize.get_range()
my_tesla.bsize.upgrade()
my_tesla.bsize.get_range()