f_location = "20260503\\10-1\\learning_python.txt"

with open(f_location) as f:
    lines = f.readlines()

for l in lines:
    print(l.strip())