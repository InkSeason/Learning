names = ['Alice', 'Bob', 'Charlie']
print(f'Please have a dinner with me, {names[0]}.')
print(f'Please have a dinner with me, {names[1]}.')
print(f'Please have a dinner with me, {names[2]}.')

# 3-5
print('\n')
print(f'{names[0]} can\'t make it to the dinner.')
names[0] = 'David'
print(f'Please have a dinner with me, {names[0]}.')
print(f'Please have a dinner with me, {names[1]}.')
print(f'Please have a dinner with me, {names[2]}.')

#  3-6
print('\n')
print('I found a bigger dinner table!')
names.insert(0, 'Eve')
names.insert(2, 'Frank')
names.append('Eli')
print(f'Please have a dinner with me, {names[0]}.')
print(f'Please have a dinner with me, {names[1]}.')
print(f'Please have a dinner with me, {names[2]}.')
print(f'Please have a dinner with me, {names[3]}.')
print(f'Please have a dinner with me, {names[4]}.')
print(f'Please have a dinner with me, {names[5]}.')

# 3-7 
print('\n')
print('I can only invite two people for dinner, cause the table won\'t arrive in time.')
print(f'Sorry, {names.pop()}, I can\'t invite you to dinner.')
print(f'Sorry, {names.pop()}, I can\'t invite you to dinner.')
print(f'Sorry, {names.pop()}, I can\'t invite you to dinner.')
print(f'Sorry, {names.pop()}, I can\'t invite you to dinner.')
print(f'Please have a dinner with me, {names[0]}.')
print(f'Please have a dinner with me, {names[1]}.')
del names[0]
del names[0]
print(names)