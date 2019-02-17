with open('guest','w') as q:
    choose=' '
    while(choose!='q'):
        name=input('enter the name:\n')
        print('fuck ' + name)
        q.write(name+'\n')
        choose=input('input q to quit,else continue')

with open('guest','a') as q:
    option=' '
    while(option!='q'):
        reason=input('enter anythiing:\n')
        q.write(reason+'\n')
        option=input('input q to quit,else continue')
