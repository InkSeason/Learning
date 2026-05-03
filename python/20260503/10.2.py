f_location = "20260503\\10-1\\learning_python.txt"

with open(f_location) as f:
    content = f.read()
    content = content.replace("python", "C++")

print(content)