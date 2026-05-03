class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.name} offers {self.type}")
    def open_restaurant(self):
        print(f"{self.name} is now opening.")
    def set_number_served(self, number):
        self.number_served = number
    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant("Cooking", "Chinese, Western, Indian")
restaurant.open_restaurant()
restaurant.set_number_served(100)
print(f"Number of customers served: {restaurant.number_served}")
restaurant.increment_number_served(50)
print(f"Number of customers served after increment: {restaurant.number_served}")

