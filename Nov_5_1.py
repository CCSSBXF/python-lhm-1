def city_f(city,country,population=0):
    if population:
        caf=city.title()+","+country.title()+'-population '+str(population)
    else:
        caf=city.title()+","+country.title()
    return caf