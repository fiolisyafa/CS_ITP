people = ["Michael Jackson", "Eminem", "Rihanna"]
message4 = "I have found a bigger table!"
print(message4)
people.insert(3, "lady Gaga")
people.insert(4, "Ed Sheeran")
people.insert(5, "Adam levine")
message3 = ", you are invited to dinner!"
for i in people:
    print(i + message3)
