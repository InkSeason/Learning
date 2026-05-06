def toppings(*materials):
    for m in materials:
        print(f"Adding {m}.")
    print("Finished making your sandwich!\n")

toppings("pepperoni")
toppings("mushrooms", "green peppers", "extra cheese")
toppings("olives", "onions", "pineapple", "ham")
