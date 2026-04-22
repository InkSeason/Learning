places = ['Suzhou', 'Shanghai', 'Beijing', 'Guangzhou', 'Shenzhen']
print(places)
print('\n')

print(sorted(places))
print(places) # 检查顺序有没有变
print('\n')

print(sorted(places, reverse = True))
print(places) # 检查顺序有没有变
print('\n')

places.reverse()
print(places)
places.reverse()
print(places)
print('\n')

places.sort()
print(places)
places.sort(reverse = True)
print(places)