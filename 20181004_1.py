prompt = '\ntell me something:'
prompt += "\nenter 'quit' to end the program."
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)

