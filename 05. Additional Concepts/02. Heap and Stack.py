def stack_example():
    a = 10  # 'a' is stored in the stack
    b = 20
    result = a + b
    return result

def heap_example():
    my_list = [1, 2, 3, 4, 5]  # 'my_list' is stored in the heap
    return my_list

print(stack_example())  # 30
print(heap_example())   # [1, 2, 3, 4, 5]
