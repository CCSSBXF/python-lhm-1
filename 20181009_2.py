magicians = ['qwe','asd','zcx']
copymagicians = []
def show_magicians(problem):
    for magician in problem:
        print('son of bitch '+magician)
    print('\n')

def make_great(magicians):
    i=0
    for magician in magicians:
         current = magicians.pop(i)
         current = 'the loser '+current
         magicians.insert(i,current)
         i+=1
    return magicians

show_magicians(magicians)
copymagicians = make_great(magicians[:])
print(magicians)
print(copymagicians)
show_magicians(magicians)
show_magicians(copymagicians)



