favorite_places={
                'zhao':['bei','shang','guang'],
                'qian':['jiang','zhe','hu'],
                'li':['fujian']
                }
for name,places in favorite_places.items():
    if len(places) == 1:
        print(name.title()+"'s favorite place is:")
        print(places)
    else:
        print(name.title()+" 's favorite place are:")
        print(places)
    print('\n')