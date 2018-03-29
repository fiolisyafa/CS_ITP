word = input()
if (word.isupper()):
    print(word.swapcase())
elif (word[0].islower() and word[1:].isupper()):
    print(word.swapcase())
elif (word.islower() and len(word) == 1):
    print(word.swapcase())
else:
    print(word)
