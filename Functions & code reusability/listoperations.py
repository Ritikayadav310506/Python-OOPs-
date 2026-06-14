from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map: square each number
squares = list(map(lambda x: x**2, numbers))

# filter: keep even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

# reduce: sum of all numbers
total = reduce(lambda x, y: x + y, numbers)

print("Squares:", squares)
print("Evens:", evens)
print("Sum:", total)
