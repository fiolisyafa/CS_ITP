usernames = ['admin', 'Lola', 'Lois', 'John', 'Sarah']
if usernames:
    for i in usernames:
        if i == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print("Hello ", i, "thank you for logging in again.")
else:
    print('We need to find some users!')

usernames = []
if usernames:
    for i in usernames:
        if i == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print("Hello ", i, "thank you for logging in again.")
else:
    print('\nWe need to find some users!')
