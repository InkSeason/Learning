class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.name} offers {self.type}")
    def open_restaurant(self):
        print(f"{self.name} is now opening.")

restaurant_1 = Restaurant('Pizza Hut', 'Italian')
restaurant_2 = Restaurant('KFC', 'Fast Food')
restaurant_3 = Restaurant('McDonald', 'Fast Food')
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()