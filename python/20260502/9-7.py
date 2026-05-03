class User:
    def __init__(self, first_name, last_name, age):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
    def describe_user(self):
        print(f"User's name is {self.f_name} {self.l_name} and age is {self.age}.")
    def greet_user(self):
        print(f"Hello, {self.f_name} {self.l_name}!")

class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privilieges = []
    def show_privilieges(self):
        print("Admin has the following privilieges:")
        for priviliege in self.privilieges:
            print(f"- {priviliege}")

admin = Admin("Alice", "Smith", 35)
admin.privilieges = ["can add post", "can delete post", "can ban users",]
admin.show_privilieges()