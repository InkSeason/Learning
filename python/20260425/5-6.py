age = 10
if age < 2 :
    print(f"The {age} years old man is a baby.")
elif age >= 2 and age < 4:
    print(f"The {age} years old man is a child.")
elif age >= 4 and age < 13:
    print(f"The {age} years old man is a kid.")
elif age >= 13 and age < 20:
    print(f"The {age} years old man is a aolescent.")
elif age >= 20 and age < 65:
    print(f"The man is a adult.")
else:
    print(f"The man is a old man.")