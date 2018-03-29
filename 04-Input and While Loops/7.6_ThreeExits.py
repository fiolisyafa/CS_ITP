#Using a conditional test
prompt = "Enter a topping you would like to add to your pizza:"
prompt += "\nEnter 'quit' when you are done. "
topping = input(prompt)
while topping != "quit":
        print("We will add", topping, "to your pizza.")

#Using an active variable
prompt = "Enter a topping you would like to add to your pizza:"
prompt += "\nEnter 'quit' when you are done. "
active = True
while active:
    topping = input(prompt)

    if topping == "quit":
        active = False
    else:
        print("We will add", topping, "to your pizza.")

#Using a break statement
prompt = "Enter a topping you would like to add to your pizza:"
prompt += "\nEnter 'quit' when you are done. "
while True:
    topping = input(prompt)
    if topping == "quit":
        break
    else:
        print("We will add", topping, "to your pizza.")
