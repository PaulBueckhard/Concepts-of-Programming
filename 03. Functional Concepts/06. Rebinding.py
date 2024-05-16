# Initial immutable data structure
initial_value = 10

# Function that returns a new value without changing the original
def increment(value):
    return value + 1

# Trying to rebind (not allowed in pure functional languages)
# initial_value = increment(initial_value)  # This would be rebinding

# Instead, we assign the result to a new variable
new_value = increment(initial_value)

print(f"Initial value: {initial_value}")  # Initial value: 10
print(f"New value: {new_value}")          # New value: 11
