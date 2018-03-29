people = ["Michael Jackson", "Eminem", "Rihanna", "Lady Gaga", "Ed Sheeran", "Adam Levine"]

five = people.pop()
four = people.pop()
three = people.pop()
two = people.pop()
uninvited = [five, four, three, two]

message = ", sorry, I can't invite you to dinner"
for i in uninvited:
    print(i + message)
message2 = ", you are still invited to dinner!"
for i in people:
    print(i + message2)

del people[1]
del people[0]
print(people)
