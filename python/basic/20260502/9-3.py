class User:
    def __init__(self, first_name, last_name, age):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
    def describe_user(self):
        print(f"User's name is {self.f_name} {self.l_name} and age is {self.age}.")
    def greet_user(self):
        print(f"Hello, {self.f_name} {self.l_name}!")

user_1 = User('John', 'Doe', 30)
user_1.describe_user()
user_1.greet_user()
