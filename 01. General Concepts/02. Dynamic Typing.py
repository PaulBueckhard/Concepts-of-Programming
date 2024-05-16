def add(a, b):
    return a + b

# Both integers
result_int = add(10, 5)
print("Adding integers:", result_int)

# Both floats
result_float = add(10.5, 5.5)
print("Adding floats:", result_float)

# A string and an integer (Will raise an error at runtime)
try:
    result_mixed = add("Hello", 5)
    print("Adding a string and an integer:", result_mixed)
except TypeError as e:
    print("Error:", e)

# Two strings
result_string = add("Hello", " World!")
print("Adding strings:", result_string)

# Example showing flexibility and type-neutral code
def process_data(data):
    # This function can handle any type of data
    print("Processing data:", data)

# Different types of data can be passed to the function without type declarations
process_data(42)
process_data(3.14)
process_data("A dynamic typed string")
process_data([1, 2, 3, 4])

