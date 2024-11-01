# Import the random module
 # type: ignore

import random

# Define known values
fruits = ['apple', 'banana','cherry','peach','plum','watermelon']

# Experiment with how random functions work
print(random.randint(3, 35))
print(random.random())
print(random.choice(fruits))
print(random.choices(fruits, k=3))
print(random.sample(fruits, k=3))
random.shuffle(fruits)
print(fruits)