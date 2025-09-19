from collections import Counter, defaultdict, namedtuple, deque

data =["apple", "banana", "orange", "apple", "orange", "banana", "apple"]
print(Counter(data)) # Counts occurrences of each element
print(Counter(data).most_common(2)) # Most common 2 elements

d = defaultdict(int) # Works like a dictionary but assign a default value for unassigned keys 
d["a"] += 1 # d["a"] is now 1 
print(d["a"]) # d["a"] is 1
print(d["b"]) # d["b"] is 0 (created automatically)

Point = namedtuple("Point", ["x", "y"]) # Creates a simple class-like structure
p = Point(11, 20) # Create an instance of Point
print(p.x, p.y) 

dq = deque([1,2,3,4]) # Double-ended queue
dq.appendleft(0) # Adds to the left end
dq.append(5) # Adds to the right end  
print(dq)