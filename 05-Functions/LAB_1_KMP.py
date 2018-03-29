def aldi():
    #inputs are in the form first-second
    names = (input())
    arrays = [names[0]]
    #this prints the letter after the dash/ first letter of each name
    for i in range(0, len(names)):
        if names[i] == "-":
            arrays.append(names[i+1])
    arr = ''
    for i in arrays:
        arr = arr + i
    print(arr.upper())
aldi()
