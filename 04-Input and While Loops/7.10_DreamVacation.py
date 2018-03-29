dream_vacation = {}
polling_active = True
while polling_active:
    name = input("What is your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")
    dream_vacation[name] = vacation
    question = input("Continue poll? ")
    if question == 'no':
        polling_active = False

print('\n----- Poll Results -----\n')
for name, vacation in dream_vacation.items():
    print(name.title(),"would like to go to", vacation.title() + ".")
