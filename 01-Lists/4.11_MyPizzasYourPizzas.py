pizza = ["cheese", "pepperoni", "hawaian"]
friends_pizzas = pizza[:]
pizza.append("marinara")
friends_pizzas.append("NY style")
print("My favorite pizzas are:")
for i in pizza:
    print(i)
print("\nMy friend's favourite pizzas are:")
for i in friends_pizzas:
    print(i)
