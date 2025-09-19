import random

print(random.random())
print(random.randint(1, 6))
print(random.uniform(1.0, 10.0))

colors = ['red', 'blue', 'green', 'yellow']
print(random.choice(colors))
print(random.choices(colors, k=3))
print(random.sample(colors, 2))

deck = [1,2,3,4,5,6]
random.shuffle(deck)
print(deck)