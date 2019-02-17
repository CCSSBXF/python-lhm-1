import json

numbers=[2,3,4,6,13,14,]

filename ='number.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
