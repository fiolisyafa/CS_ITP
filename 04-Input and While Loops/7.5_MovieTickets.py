while True:
    age = input("Enter your age: ")
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket is $10.")
    elif age > 12:
        print("Your ticket is $15")
