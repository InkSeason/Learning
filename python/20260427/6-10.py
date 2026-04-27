favorite_numbers = {
    'Alice': [3, 7, 9],
    'Bob': [2, 4, 6],
    'Charlie': [1, 5, 8],
}

for people,num in favorite_numbers.items():
    if len(num) == 1:
        print(f"\n{people}'s favorite number is {num[0]}.")
    else:
        print(f"\n{people}'s favorite numbers are {', '.join(str(n) for 
    n in num)}.")
