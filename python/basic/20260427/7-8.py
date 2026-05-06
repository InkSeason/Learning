sandwich_orders = ['pastrami', 'veggie', 'pastrami', 'turkey', 
'roast beef', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwiches.append(sandwich_orders.pop())
    print(f"Making a {finished_sandwiches[-1]} sandwich.")

print("\nWe have made the following sandwiches: ")
print(f"{' sandwich, '.join(finished_sandwiches).title()}.")