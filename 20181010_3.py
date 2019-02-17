def make_cars(a,b,**cars_info):
    cars={}
    cars['q']=a
    cars['w']=b
    for key,value in cars_info.items():
        cars[key]=value
    return cars

car=make_cars('subaru','outback',color='blue',two_package=True)
print(car)