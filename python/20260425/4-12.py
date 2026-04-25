my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('KFC')
friend_foods.append('McDonalds')
print("My favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)