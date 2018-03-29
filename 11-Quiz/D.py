num = int(input())
for i in range(num):
    var = input()
    if len(var) > 10:
        print(var.replace(var[1:-1], str(len(var)-2)))
    else:
        print(var)
