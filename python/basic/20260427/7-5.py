while True:
    age = input("Please enter your age: ")
    age = int(age)
    if age < 3:
        print("You are a baby. Your admission is free.")
        break
    elif age < 12:
        print("You are a child. Your admission is $10.")
        break
    else:
        print("You are an adult. Your admission is $15.")
        break