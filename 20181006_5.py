want_to={}
while True:
    place = input('\nwhere would you go?')
    name = input('what your name?')
    want_to[name]=place
    repeat = input('anyone else?')
    if repeat == 'no':
        break

print('****************')
for name,place in want_to.items():
    print(name+' want to '+place)
