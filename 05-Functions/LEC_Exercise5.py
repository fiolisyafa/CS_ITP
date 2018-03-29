def calculator(num1,  num2, opp="+", out="float"):
    try:
        if opp == "+":
            result = num1 + num2
        elif opp == "-":
            result = num1 - num2
        elif opp == "*":
            result = num1 * num2
        elif opp == "/":
            result = num1 / num2

        if out == "float" or opp == "/":
            return float(result)
        elif out == "int":
            return round(result)

    except ValueError:
        return None

print(calculator(2, 3.0))
print(calculator(2, 3.0, out="int"))
print(calculator(2, 3.0, "/"))
print(calculator(2, 3.0, "/", "int"))
