f_location = "20260503\\10-1\\learning_python.txt"

with open(f_location) as f:
    for l in f:
        print(l.strip())