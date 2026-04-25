pizzas = ['pepperoni', 'hawaiian', 'cheese']
my_pizzas = pizzas[:]
pizzas.append('veggie')
my_pizzas.append('meat lovers')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
    