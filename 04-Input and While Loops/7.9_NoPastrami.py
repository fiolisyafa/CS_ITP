sandwich_orders = ['baloney', 'pastrami', 'PBnJ', 'meatball', 'pastrami', 'tuna', 'chicken', 'pastrami',]
print("The deli has run out of pastrami.")
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("I made your", sandwich_order, "sandwich.")
    finished_sandwiches.append(sandwich_order)
