# Function that takes another function as an argument
def apply_operation(func, value):
    return func(value)

# Example functions to be passed
def square(x):
    return x * x

def increment(x):
    return x + 1

# Using the higher-order function
print(apply_operation(square, 5))   # 25
print(apply_operation(increment, 5))  # 6

# Function that returns another function
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

# Creating and using a multiplier function
double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
