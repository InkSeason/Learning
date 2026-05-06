sandwich_orders = ['pastrami', 'veggie', 'pastrami', 'turkey', 
'roast beef', 'pastrami']

print("Sorry, we are out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []

while sandwich_orders:
    finished_sandwiches.append(sandwich_orders.pop())
    print(f"Making a {finished_sandwiches[-1]} sandwich.")

print("\nWe have made the following sandwiches: ")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich.")

