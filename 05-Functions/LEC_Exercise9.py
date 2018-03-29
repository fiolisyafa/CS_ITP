def gen(n):
    while n > 0:
        yield n
        n -= 1
for x in gen(100):
    print(x)
