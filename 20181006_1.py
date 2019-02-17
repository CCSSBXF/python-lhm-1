caidan = ['a','b','c','d','e']
active = True
prompt = 'which are you want\n'
while active:
    print('press quit to end,else to add')
    prompt = input(prompt)
    if prompt == 'quit':
        break
    if prompt not in caidan:
        print('without')
        continue
    else:
        print('done')

