# Recursive function to calculate the sum of a list
def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])

# Higher-order function to filter even numbers
def filter_even(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

numbers = [1, 2, 3, 4, 5, 6]

sum_result = recursive_sum(numbers)
even_numbers = filter_even(numbers)

print(f"Sum of numbers: {sum_result}")  # Sum of numbers: 21
print(f"Even numbers: {even_numbers}")  # Even numbers: [2, 4, 6]
