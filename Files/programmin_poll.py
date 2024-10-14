filename = 'programming_poll.txt'

responses = []
while True:
    response = input("Why you like programming? (q to quit) ")
    if response.lower() == 'q':
        break
    responses.append(response)

with open(filename, 'a') as file_object:
    for response in responses:
        file_object.write(f"{response}\n") 