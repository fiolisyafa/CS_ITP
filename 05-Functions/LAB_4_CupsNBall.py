swaps = input()
place = [1, 0, 0]
#aldi is the function that switches the cups
def aldi(x, y):
    place[x], place[y] = place[y], place[x]
for i in swaps:
    #the values of x and y are changed according to the index of the cups that are switched
    if i == "A":
        aldi(0, 1)
    if i == "B":
        aldi(1, 2)
    if i == "C":
        aldi(0, 2)
#in the list, 1 means the ball is under the cup, 0 means the cup is empty
print(place.index(1) + 1)
