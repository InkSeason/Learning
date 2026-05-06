dreaming_resorts = {}
flag = True
while flag:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world," \
    " where would you go? ")
    dreaming_resorts[name] = place
    repeat = input("Would you like to let another person " \
    "respond? (yes/no) ")
    if repeat == 'no':
        flag = False
        
print("\n--- Poll Results ---")
for name, place in dreaming_resorts.items():
    print(f"{name} would like to visit {place}.")