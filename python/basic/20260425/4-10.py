pizzas = ['pepperoni', 'hawaiian', 'cheese', 'veggie', 'meat lovers', 
          'bbq chicken']

print("The first three items in the list are:")
for pizza in pizzas[:3]:
    print(pizza)
print("\nThe middle three items in the list are:")
for pizza in pizzas[1:4]:
    print(pizza)
print("\nThe last three items in the list are:")
for pizza in pizzas[-3:]:
    print(pizza)