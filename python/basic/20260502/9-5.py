class User:
    def __init__(self, first_name, last_name, age):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        self.login_attempts = 0
    def describe_user(self):
        print(f"User's name is {self.f_name} {self.l_name} and age is {self.age}.")
    def greet_user(self):
        print(f"Hello, {self.f_name} {self.l_name}!")
    def login_attempts_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("John", "Doe", 30)
user.describe_user()
user.greet_user()
print(f"Login attempts: {user.login_attempts}")
user.login_attempts_attempts()
user.login_attempts_attempts()
print(f"Login attempts after increment: {user.login_attempts}")
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")


