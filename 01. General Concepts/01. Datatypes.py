int_var = 42            # Integer type, represents a whole number, (e.g., -2, -1, 0, 1, 2, ...)
float_var = 3.14        # Floating point type, represents a real number, (e.g., -2.5, 0.0, 3.14, ...)
bool_var = True         # Boolean type, represents a logical state, True or False
string_var = "Hello"    # String type, represents a sequence of characters, (e.g., "Hello", "World")

# Representation: Physical bit storage
import sys
print("Size of int:", sys.getsizeof(int_var), "bytes")
print("Size of float:", sys.getsizeof(float_var), "bytes")
print("Size of bool:", sys.getsizeof(bool_var), "bytes")
print("Size of string:", sys.getsizeof(string_var), "bytes")

# Behavior: Operations that can be performed on the data
# Integers and floats can be used in arithmetic operations
sum_result = int_var + float_var
print("Sum of int and float:", sum_result)

# Booleans can be used in logical operations
bool_result = bool_var and False
print("Logical AND result:", bool_result)

# Strings can be concatenated and manipulated
string_result = string_var + ", World!"
print("Concatenated string:", string_result)
