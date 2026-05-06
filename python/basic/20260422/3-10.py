storages = ['backpack', 'satchel', 'pocket']
print(f"You have a {storages[0]}, a {storages[1]}, and a {storages[2]} to carry your items.")
print(f"You have {len(storages)} storage options.")
print(storages)

print("However, you cannot carry digital items")
storages.insert(0, 'USB')
storages.append('cloud')
print("You thought of a way to carry digital items, so you added a USB and cloud storage to your options.")
print(f"You now have {len(storages)} storage options.")
print(storages)
print(f"Now you have a {storages[0]}, a {storages[1]}, a {storages[2]}, a {storages[3]}, and a {storages[-1]} to carry your digital items.")

print("You realize that you don't need the pocket, so you remove it from your options.")
del storages[2]
print(f"You now have {len(storages)} storage options.")
print(storages)

print("Alice needs storage for her items, so you give her your backpack.")
Alice_storage = storages.pop(0)
print(f"You gave Alice your {Alice_storage}.")
print(f"You now have {len(storages)} storage options.")
print(storages)

print("Now you should to sort your storage options.")
storages.sort()
print(f"Your sorted storage options are: {storages}")
storages.sort(reverse=True)
print(f"Your reverse-sorted storage options are: {storages}")