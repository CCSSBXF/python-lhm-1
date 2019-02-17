responses = {}
polling_active = True
while polling_active :
    name = input('\nWhat is your name? ')
    response = input('which mountain would you like ti climb someday?')
    responses[name]=response
    repeat = input('would you like to let another person respond?(yes/no)')
    if repeat == 'no':
        polling_active = False
print('\n-- poll results --')
for name,response in responses.items():
    print(name+' would like to climb '+response)