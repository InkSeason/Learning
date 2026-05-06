f_name = '20260503\\10-3_and_10-4\\name.txt'

name = input("What is your name? ")

with open(f_name, 'w') as f:
    f.write(name)
