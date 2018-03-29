n = int(input())
number = 0
for i in range(n):
    statement = input()
    if (statement.lower() == "++x") or (statement.lower() == "x++"):
        number += 1
    elif (statement.lower() == "--x") or (statement.lower() == "x--"):
        number -= 1
print(number)
