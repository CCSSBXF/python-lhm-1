import json

filename='favoritenumber.json'

def get_n():
    fn=input('what is your favorite number')
    with open(filename,'w') as f_obj:
        json.dump(fn,f_obj)

def put_n():
    with open(filename) as f_obj:
        fn=json.load(f_obj)
        print('it is '+fn)

def show():
    try:
        with open(filename) as f_obj:
            fn=json.load(f_obj)
    except FileNotFoundError :
        get_n()
    else:
        put_n()

show()