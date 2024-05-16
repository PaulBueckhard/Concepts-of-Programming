class Maybe:
    def __init__(self, value):
        self.value = value

    def is_nothing(self):
        return self.value is None

    def bind(self, func):
        if self.is_nothing():
            return self
        return Maybe(func(self.value))

    def __repr__(self):
        if self.is_nothing():
            return 'Nothing'
        return f'Just({self.value})'

# Example functions to use with Maybe monad
def safe_divide(x, y):
    if y == 0:
        return None
    return x / y

def add_ten(x):
    return x + 10

# Example usage
result = Maybe(20).bind(lambda x: safe_divide(x, 2)).bind(add_ten)
print(result)  # Just(20.0)

result = Maybe(20).bind(lambda x: safe_divide(x, 0)).bind(add_ten)
print(result)  # Nothing
