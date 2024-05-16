int_var = 42
float_var = 3.14
string_var = "123"

# Convert integer to float
int_to_float = float(int_var)
print("Integer to float:", int_to_float)  # 42.0

# Convert float to integer
float_to_int = int(float_var)
print("Float to integer:", float_to_int)  # 3

# Convert string to integer
string_to_int = int(string_var)
print("String to integer:", string_to_int)  # 123

# Convert integer to string
int_to_string = str(int_var)
print("Integer to string:", int_to_string)  # "42"

# Adding an integer and a float
result = int_var + float_var  # Automatic type conversion: int to float
print("Adding integer and float:", result)  # 45.14

# Concatenating string and integer (after conversion)
result_string = string_var + str(int_var)
print("Concatenating string and integer:", result_string)  # "12342"

# Example: User input conversion
user_input = input("Enter a number: ")
# Convert user input (string) to integer for arithmetic operation
user_number = int(user_input)
print("User entered number plus 10:", user_number + 10)
