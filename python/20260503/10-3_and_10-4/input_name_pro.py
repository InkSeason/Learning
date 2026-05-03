f_name = '20260503\\10-3_and_10-4\\name.txt'
flag = True

with open(f_name, 'w') as f:
    while flag:
        name = input("Please enter your name(enter 'quit' to exit): ")
        if name == "quit":
            flag = False
            break
        else:
            print(f"Hello, {name}!")
            f.write(f"guest name: {name}\n")