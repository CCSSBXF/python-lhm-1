cities={'fujian':{"country":'china','population':1400000000,'fact':'beautiful'},
        'newyo':{'country':'america','population':124501000,"fact":'nice'},
        'london':{'country':'UK','population':98415201,'fact':'cool'}
        }
for city,information in cities.items():
    print(city+'\n')
    for key,value in information.items():
        print('\t'+key)
        print('\t\t'+str(value))
