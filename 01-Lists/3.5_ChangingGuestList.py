people = ["Michael Jackson", "Beyonce", "Rihanna"]
message3 = ", you are invited to dinner!"
print(people[1] + " cannot make it.")
people[1] = "Eminem"
print(people[0] + message3), print(people[1] + message3), print(people[2] + message3 + '\n')

#alternative
for i in people:
    print(i + message3)
