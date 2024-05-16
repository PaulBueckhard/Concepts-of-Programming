# Immutable data structure: Tuple
numbers = (1, 2, 3, 4, 5)

# Idempotent function: No side effects
def square(x):
    return x * x

# Referential transparency: Expression can be replaced with its value
squared_numbers = list(map(square, numbers))

print(squared_numbers)  # [1, 4, 9, 16, 25]
