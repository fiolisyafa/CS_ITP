def aldi():
    mod = []
    #the program accepts 10 numbers
    for i in range(0, 10):
        i = int(input())
        #modul 42 of each input will be appended to the empty list
        output = i % 42
        mod.append(output)
    #print the number of distinct modules.
    print(len(set(mod)))
aldi()
