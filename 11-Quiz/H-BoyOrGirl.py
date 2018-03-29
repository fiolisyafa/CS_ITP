user = input()
if len(user) % 2 == 0 and user.islower():
    print("CHAT WITH HER!")
elif len(user) % 2 != 0 and user.islower():
    print("IGNORE HIM!")
