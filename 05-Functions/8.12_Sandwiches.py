def make_sandwich(*ingredients):
    print('Your sandwich will contain the following ingredients:')
    for ingredient in ingredients:
        print('-', ingredient)

make_sandwich('tuna', 'lettuce', 'tomato')
make_sandwich('chicken', 'mayo', 'lettuce')
make_sandwich('meatball', 'cheddar', 'jalapeno', 'lettuce')
