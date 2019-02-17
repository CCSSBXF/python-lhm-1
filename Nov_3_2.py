from Nov_3_1 import gfn

print('enter q to quit')
while True:
    first=input('first name:')
    if first=='q':
        break
    last=input('last name:')
    if last=='q':
        break
    fn=gfn(first,last)
    print('\t neatly fotmatted name:'+fn)