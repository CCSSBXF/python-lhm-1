filename='pi.txt'
with open(filename) as file_object:
    lines=file_object.readlines()

pi_string=' '
for line in lines:
    pi_string+=line.rstrip()


print(pi_string[:20])
print(len(pi_string))
pi_string.replace('sdfh','qwer')
print(pi_string.replace('sdfh','qwer'))
message='asdfgh'
print(message.replace('asd','qwer'))