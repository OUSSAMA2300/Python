# Using break
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you finish) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to", city.title(),"!")