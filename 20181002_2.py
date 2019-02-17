rivers={'huanghe':'china',
        'nile':'egypt',
        'changjiang':'china',
        'mixixibi':'american'
        }
for river,country in rivers.items():
    print('The '+river.title()+' runs through '+country.title())
print('\n')
for river in rivers.keys():
    print(river.title())
print('\n')
for country in rivers.values():
    print(country.title())
print('\n')
countrys=['china','american']
for country in set(rivers.values()):
    print(country.title())
    if country in countrys:
        print('great')
    else:
        print('low')
print('\n')

