print('gice me two numbers,and i will divide them')
print('enter q to quit')
while True:
    first_n=input('\nfirst number:')
    if first_n=='q':
        break
    second_n=input('\nsecond number:')
    if second_n=='q':
        break
    try:
        answer=int(first_n)/int(second_n)
    except ZeroDivisionError :
        print("you can't dicide by zero!")
    else:
        print(answer)





