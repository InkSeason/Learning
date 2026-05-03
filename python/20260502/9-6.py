class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.name} offers {self.type}")
    def open_restaurant(self):
        print(f"{self.name} is now opening.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    def display_flavors(self):
        print(f"{self.name} offers the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")
    def add_flavor(self, *flavor):
        flavor_tuple = flavor
        flavor_list = list(flavor_tuple)
        while flavor_list:
            f = flavor_list.pop()
            self.flavors.append(f)
        del flavor_tuple
        del flavor_list

ice_cream_stand = IceCreamStand("Sweet Treats", "Ice Cream")
ice_cream_stand.add_flavor("Vanilla","Chocolate", "Strawberry", "Mint")
ice_cream_stand.display_flavors()