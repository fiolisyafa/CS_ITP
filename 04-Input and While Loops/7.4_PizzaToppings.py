prompt = "Enter a topping you would like to add to your pizza:"
prompt += "\nEnter 'quit' when you are done. "
while True:
    topping = input(prompt)
    if topping == "quit":
        break
    else:
        print("We will add", topping, "to your pizza.")
