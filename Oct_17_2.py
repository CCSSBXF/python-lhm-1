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
