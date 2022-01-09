class Restaurant:
    def __init__(self, restaurant_name, cruisine_type):
        self.restaurant_name = restaurant_name
        self.cruisine_type = cruisine_type
    def describe_restaurant(self):
        print(f'The restaurant name is {self.restaurant_name}, and it is a {self.cruisine_type}-styled restaurant.')
    def open_restaurant(self):
        print(f'The restaurant is open right now!')
