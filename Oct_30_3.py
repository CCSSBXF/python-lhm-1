print('number add number')
print('enter q to quit')
while True:
    first_n=input('first number:')
    if first_n=='q':
        break
    second_n=input('second number:')
    if second_n=='q':
        break
    try:
        answer=int(first_n)+int(second_n)
    except ValueError:
        print('must be numbers')
    else:
        print(answer)