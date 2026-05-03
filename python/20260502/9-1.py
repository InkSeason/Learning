class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.name} offers {self.type}")
    def open_restaurant(self):
        print(f"{self.name} is now opening.")

restaurant = Restaurant("Cooking", "Chinese, Western, Indian")
restaurant.open_restaurant()