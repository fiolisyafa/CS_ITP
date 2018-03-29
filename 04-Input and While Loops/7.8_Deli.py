sandwich_orders = ['baloney', 'PBnJ', 'meatball', 'tuna', 'chicken',]
finished_sandwiches = []
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("I made your", sandwich_order, "sandwich.")
    finished_sandwiches.append(sandwich_order)
