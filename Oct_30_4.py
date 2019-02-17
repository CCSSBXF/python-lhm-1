def output(filename):
    try:
        with open(filename) as fs:
            for f in fs:
                print(f.rstrip())
    except FileNotFoundError :
        #print(filename+' is not found')
        pass
output('cat.txt')
output('dog.txt')
output('qwe')