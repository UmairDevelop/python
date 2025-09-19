from itertools import count, cycle, repeat, chain, combinations, permutations, product, groupby
for i in count(10, 2): # Start from 10, step by 2
    print(i)
    if i >= 20:
        break

colors = cycle(["red", "green", "blue"]) # Cycles through the list indefinitely
for _ in range(6): # Print and repeat colors 6 times
    print(next(colors))

for x in repeat("A", 4): # Repeats "A" 4 times
    print(x)

print(list(chain([1,2],[3,4],[5]))) # Chains multiple iterables into one

print(list(combinations([1,2,3],2))) # All possible pairs from the list 

print(list(permutations([1,2,3],2))) # All possible ordered pairs from the list

print(list(product([1,2], ["A","B"]))) # Cartesian product of two lists

data = [("A", 1), ("B", 2), ("B", 1), ("B", 2)] # Group by first element
for key, group in groupby(data, key=lambda x: x[0]): 
    print(key, list(group))