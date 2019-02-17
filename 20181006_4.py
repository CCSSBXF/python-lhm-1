sandwich_orders = ['a','b','c','p','d','p','e','p']
finished_sandwiches = []
print('p had finished')
while sandwich_orders :
    sandwich = sandwich_orders.pop()
    print('i made '+sandwich+' for you ')
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)
while 'p' in finished_sandwiches :
    finished_sandwiches.remove('p')
print(finished_sandwiches )