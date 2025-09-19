import random

print(random.random()) # Gives a random float between 0.0 to 1.0
print(random.randint(1, 6)) # Gives a random integer between 1 to 6 (both inclusive)
print(random.uniform(1.0, 10.0)) # Gives a random float between 1.0 to 10.0

colors = ['red', 'blue', 'green', 'yellow']
print(random.choice(colors)) # Randomly selects one item from the array
print(random.choices(colors, k=3)) # Randomly selects 3 items from the array (with duplicate items possible)
print(random.sample(colors, 2)) # Randomly selects 2 items from the array (without duplicate items)

deck = [1,2,3,4,5,6]
random.shuffle(deck) # Shuffles the array randomly
print(deck)