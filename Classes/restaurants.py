# create class called restaurant

class Restaurant:
    '''Restaurant name and food type'''
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}.')

    def rest_open(self):
        print(f'{self.rest_name} is open.')


# Create three instances of the class for different types of restaurant

weedys = Restaurant('Weedy\'s', 'American fast food')
appleb = Restaurant('Applebapple\'s', 'American casual dining')
tacob = Restaurant('Taco Baco', 'Mexican-American fast food')

# Display the results, call describe rest and rest open

weedys.describe_rest()
weedys.rest_open()
appleb.describe_rest()
appleb.rest_open()
tacob.describe_rest()
tacob.rest_open()