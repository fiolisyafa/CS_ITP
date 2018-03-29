def aldi():
    stones = input()
    #see if the input is even or odd
    if int(stones) % 2 == 0:
        print("Bob")
    if int(stones) % 2 != 0:
        print("Alice")
aldi()
