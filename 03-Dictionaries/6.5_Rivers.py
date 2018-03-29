rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Mississippi': 'USA',
}
for key, value in rivers.items():
    print("The", key, "River runs through", value + ".")
for key in rivers:
    print(key)
for values in rivers.values():
    print(values)
