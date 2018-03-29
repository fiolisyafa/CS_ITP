favorite_places = {
    "Natasya": ["Korea", "HongKong", "Japan"],
    "Maria": ["Surabaya", "Lombok", "Bali"],
    "Miranda": ["Amsterdam", "Belgium", "Netherlands"],
    }
for name, places in favorite_places.items():
    print('\n' + name)
    for place in places:
        print('\t' + place)
